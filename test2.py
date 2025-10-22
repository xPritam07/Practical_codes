from flask import Flask, request, redirect

app = Flask(__name__)

users = {
    "admin": '1234',
    "pritam": '12345'
}

@app.route("/", methods=['GET','POST'])
def about_page():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        if name in users.keys() and password == users[name]:
            return redirect('/welcome')
        else:
            return '''
            <h1>Hello! Please give corresct info.</h1>
            <form method='POST'>
                <label for="name">Name</label>
                <input type="text" name="name">
                <br>
                <label for="password">Password</label>
                <input type="password" name="password">
                <br>
                <input type="submit" value="Submit">
            </form>
            '''
    return '''
        <h1>Hello!</h1>
        <form method='POST'>
            <label for="name">Name</label>
            <input type="text" name="name">
            <br>
            <label for="password">Password</label>
            <input type="password" name="password">
            <br>
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/welcome')
def welcome():
    return f'''
                <h1>Hello! Good morning from CC Lab.</h1>
            '''

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')