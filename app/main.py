from flask import Flask, request, jsonify
from app import create_app
from database.database import db
from model.models import Book
from schema.schemas import BookSchema

app = create_app()


@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()
    book_schema = BookSchema()
    book_data = book_schema.load(data)
    new_book = Book(**book_data)

    db.session.add(new_book)
    db.session.commit()

    return jsonify(book_schema.dump(new_book)), 201


@app.route("/books/<int:book_id>", methods=["GET"])
def read_book(book_id):
    book = Book.query.get_or_404(book_id)
    book_schema = BookSchema()
    return jsonify(book_schema.dump(book))


@app.route("/books", methods=["GET"])
def read_books():
    books = Book.query.all()
    book_schema = BookSchema(many=True)
    return jsonify(book_schema.dump(books))


@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json()
    book_schema = BookSchema()
    book_data = book_schema.load(data, partial=True)

    for key, value in book_data.items():
        setattr(book, key, value)

    db.session.commit()
    return jsonify(book_schema.dump(book))


@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully"}), 204


if __name__ == "__main__":
    app.run(debug=True)