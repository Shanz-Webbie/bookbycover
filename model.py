from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement= True, primary_key=True)
    user_email = db.Column(db.String, unique=True)
    user_password = db.Column(db.String)
    user_first_name = db.Column(db.String)
    user_last_name = db.Column(db.String)
    created_at = db.Column(db.Datetime)
    favorites = db.relationship("Favorites", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email} first_name={self.user_first_name} last_name={self.user_last_name}>"

class Favorite(db.Model):
    """A favorited book."""

    __tablename__ = "favorites"

    favorite_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.book_id"))
    # when was the favorite created
    created_at = db.Column(db.Datetime)
    # # if/when was the favorite deleted
    # deleted_at = db.Column(db.Datetime, nullable=True, default=None)
    user = db.relationship("User", back_populates="favorites")
    book = db.relationship("Book", back_populates="favorites")

    def __repr__(self):
        return f"<Favorite favorite_id={self.favorite_id}>"

class Book(db.Model):
    """A book."""

    __tablename__ = "books"

    book_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    book_title = db.Column(db.String)
    author_name = db.Column(db.String)
    publish_date = db.Column(db.Datetime)

    favorites = db.relationship("Favorites", back_populates="book")
    book_genres = db.relationship("BookGenre", back_populates="book")

    def __repr__(self):
        return f"<Book book_id={self.book_id} book_title={self.book_title} author_name={self.author_name}>"

class BookGenre(db.Model):
    """A middle table for book and genre."""

    __tablename__ = "bookgenre"

    bookgenre_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.book_id"))
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.genre_id"))


    books = db.relationship("Books", back_populates="bookgenre")

    def __repr__(self):
        return f"<BookGenre bookgenre_id={self.bookgenre_id}>"

class Genre(db.Model):
    """A middle table for book and genre."""

    __tablename__ = "genre"

    genre_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    genre_name = db.Column(db.String)
    is_fiction = db.Column(db.Bool)


    book_genres = db.relationship("BookGenre", back_populates="genre")

    def __repr__(self):
        return f"<Genre genre_id={self.genre_id}>"



def connect_to_db(flask_app, db_uri="postgresql:///bookbycover", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)

    # Call this here so we don't have to worry about calling it every time
    # we run model.py interactively.
    app.app_context().push()