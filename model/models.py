from database.database import db

class Book(db.Model):
    tablename = "books"

    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String, index=True)
    author = db.Column(db.String, index=True)
    published_year = db.Column(db.Integer)