from flask import Flask, request, redirect

app = Flask(__name__)

fd = []

@app.route("/", methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        feedb = request.form.get('feedback')
        if len(feedb)>=5:
            fd.append(feedb)
            return redirect("/thank")
        else:
            return """
                    <center>
                    <h2>Give a vaild feedback</h2>
                    <form method = 'post'>
                        Feedback <input type="text" name="feedback" required><br>
                        <input type='submit' value='Give Feedback'>
                    </form>
                    </center>
                    """ 
    return """
            <center>
            <h2>Feedback Form</h2>
            <form method = 'post'>
            Feedback <input type="text" name="feedback" required><br>
            <input type='submit' value='Give Feedback'>
            </form>
            </center>
            """

@app.route("/thank")
def thank_page():
    return f"""
            <center>
            <h1>Thank you for your Feedback</h1>
            <h2>You feedback is:</h2><br>
            <p>{fd[-1]}</p>
            <a href="/"><button>Go back</button></a>
            </center>
            """
if __name__ == "__main__":
    app.run(debug=True)