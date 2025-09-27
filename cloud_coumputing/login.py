from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


credentials = {
    "admin":"admin123",
    "pritam":"pg5772",
    "karamveer": "ks9673",
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in credentials.keys() and password == credentials[username]:
            return redirect("/welcome")
        else:
            return '''
            <form method="post">
            <center>
            <h2>Invalid Credentials! Try again.</h2>
            <br>
            Username: <input type="text" name="username" required><br>
            Password: <input type="password" name="password" required><br>
            <input type="submit" value="Login">
            </center>
            </form>
            '''
    return '''
    <form method="post">
    <center>
    Username: <input type="text" name="username" required><br>
    Password: <input type="password" name="password" required><br>
    <input type="submit" value="Login">
    </center>
    </form>
    '''

@app.route("/welcome")
def welcome():
    return '''
    <h2>Welcome! You are successfully logged in.</h2>
    <a href="/"><button>Go back</button></a>
    '''

if __name__ == "__main__":
    app.run(debug=True)