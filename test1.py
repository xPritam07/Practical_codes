from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        q1 = request.form.get("q1")
        score = 1 if q1 == "Cloud Computing" else 0
        return f"<h2>The Score is {score}<h2>"
    return '''
<h2>Simple Quiz</h2>
    <form method="post">
        Q1: Which technology provides on-demand computing resources over the internet?<br>
        <input type="radio" name="q1" value="Cloud Computing"> Cloud Computing<br>
        <input type="radio" name="q1" value="Networking"> Networking<br>
        <input type="radio" name="q1" value="OS"> Operating System<br>
        <input type="submit" value="Submit">
    </form>
'''
if __name__ == "__main__":
    app.run(debug=True)