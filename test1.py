from flask import Flask, request, redirect

app = Flask(__name__)

user_data = {
    "admin":"admin123",
    "Pritam": "pg5772",
    "Susmita": "sg8701"
}

@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in user_data.keys() and password == user_data[username]:
            return f"<center><h2>Welcome! You logged in successfully.<h2></center>"
        else:
            return'''
<center>
<h2>Wrong Credentials! Login to continue.<h2>
<form method ='POST'>
Username <input type="text" name="username" required /><br>
Password <input type="password" name="password" required /><br>
<input type="submit" value="Login">
</from>
</center>
'''
    return '''
<center>
<h2>Login Form<h2>
<form method ='POST'>
Username <input type="text" name="username" required /><br>
Password <input type="password" name="password" required /><br>
<input type="submit" value="Login">
</from>
</center>
'''

if __name__ == "__main__":
    app.run(debug=True)