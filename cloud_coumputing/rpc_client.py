from jsonrpclib import Server

input_string = input("Give your input: ")

def main():
    conn = Server("http://localhost:1086")
    print(f"The sentiment is: {conn.check_sentiment(input_string)}")

if __name__ == '__main__':
    main()