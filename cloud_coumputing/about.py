from flask import Flask

app = Flask(__name__)

@app.route("/")
def about():
    return '''
    <h2>About Me</h2>
    <p>Name: John Doe</p>
    <p>Department: Computer Science</p>
    <p>Interests: Cloud Computing, AI, Web Development</p>
    '''

if __name__ == "__main__":
    app.run(debug=True)