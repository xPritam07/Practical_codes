from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {'id':1, "title":"Book1", "author":"Author1"},
    {'id':2, "title":"Book2", "author":"Author2"},
    {'id':3, "title":"Book3", "author":"Author3"}
]

@app.route("/", methods=['GET', 'POST'])
def get_books():
    return '''
    <a href='/allBooks'><button>All Books</button></a>

    <h2>Get a Particular book</h2>
    <form method='post'>
'''

@app.route("/book/<int:book_id>",methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}),404
    return jsonify(book)

@app.route("/allBooks")
def allbooks():
    return jsonify({"Books": books})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug='True')