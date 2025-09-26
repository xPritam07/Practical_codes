import boto3
import json
import urllib.request
import time
from IPython.display import Audio, display

# Initialize clients
textract = boto3.client('textract')
comprehend = boto3.client('comprehend')
translate = boto3.client('translate')
transcribe = boto3.client('transcribe')
polly = boto3.client('polly')
s3 = boto3.resource('s3')

def extract_text_from_pdf(bucket_name, document_name):
    response = textract.detect_document_text(
        Document={'S3Object': {'Bucket': bucket_name, 'Name': document_name}}
    )
    text = [item['Text'] for item in response['Blocks'] if item['BlockType'] == 'LINE']
    return '\n'.join(text)


# Replace with your bucket and file
bucket_name = "lab-data-bucket-227847886297-c460db80"
document_name = "ABC_Corporation.pdf"
extracted_text = extract_text_from_pdf(bucket_name, document_name)
print("Extracted Text:\n", extracted_text[:1500])


def analyze_sentiment(text):
    response = comprehend.detect_sentiment(
        Text=text[:5000],  # Comprehend limit
        LanguageCode='en'
    )
    return response


sentiment_result = analyze_sentiment(extracted_text)
print("Sentiment Analysis Result:")
print(json.dumps(sentiment_result, indent=2))

def translate_text(text, target_lang='es'):
    response = translate.translate_text(
        Text=text[:5000],
        SourceLanguageCode='auto',
        TargetLanguageCode=target_lang
    )
    return response['TranslatedText']


translated_text = translate_text(extracted_text, 'fr')
print("Translated Text (French):\n", translated_text[:1500])

def text_to_speech(text, filename):
    response = polly.synthesize_speech(
        Text=text[:3000],
        OutputFormat='mp3',
        VoiceId='Joanna'
    )

    # Get the audio stream content
    audio_stream = response['AudioStream'].read()

    # Upload to S3
    s3.Object(bucket_name, f"audio-output/{filename}.mp3").put(
        Body=audio_stream
    )

    print(f"Audio saved: s3://{bucket_name}/audio-output/{filename}.mp3")

    # Create audio player with the audio data directly
    return Audio(data=audio_stream, autoplay=False)


# Call the function and display the audio player
audio_player = text_to_speech(extracted_text[:3000], "lab-output")
display(audio_player)

def transcribe_audio(audio_file):
    job_name = "lab-transcription-job"
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': f"s3://{bucket_name}/audio-output/{audio_file}"},
        MediaFormat='mp3',
        LanguageCode='en-US'
    )
    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        time.sleep(5)
    
    # Get the transcript text from the JSON file
    if status['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
        transcript_uri = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
        response = urllib.request.urlopen(transcript_uri)
        data = json.loads(response.read())
        return data['results']['transcripts'][0]['transcript']
    else:
        return "Transcription failed"

audio_file_name = "lab-output.mp3"
transcript_text = transcribe_audio(audio_file_name)
print("Transcription Text:", transcript_text)

def diy_polly_conversion(text, filename):

    # TODO: Modify this function
    response = polly.synthesize_speech(
        Text=text[:3000],
        OutputFormat='<replace>',
        VoiceId='Matthew'
    )

    # Get the audio stream content
    audio_stream = response['AudioStream'].read()

    # TODO: Modify this function
    s3.Object(bucket_name, f"diy-output/{filename}.mp3").put(
        Body="<replace>"
    )

    print(f"Audio saved: s3://{bucket_name}/diy-output/{filename}.mp3")

    # Create audio player with the audio data directly
    return Audio(data=audio_stream, autoplay=False)


# Call the function and display the audio player
audio_player = diy_polly_conversion(extracted_text[:3000], "diy-result")
display(audio_player)