from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def quiz():
    if request.method == "POST":
        dob_str = request.form['dob']
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return f"<h3>Your age is {age}</h3>"
    return '''
        <h1>Quiz page</h1>
        <form method='post'>
            <label for="dob">Date of birth</label>
            <input type="date" name="dob" required>
            <input type="submit" value="Check Age">
        </form>
        '''

if __name__ == "__main__":
    app.run(debug=True)