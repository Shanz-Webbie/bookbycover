from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import PrimaryKeyConstraint

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement= True, primary_key=True)
    user_email = db.Column(db.String, unique=True)
    user_password = db.Column(db.String)
    user_first_name = db.Column(db.String)
    # user_last_name = db.Column(db.String)
    created_at = db.Column(db.DateTime)

    favorites = db.relationship("Favorite", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.user_email} first_name={self.user_first_name} last_name={self.user_last_name}>"


class Book(db.Model):
    """A book."""

    __tablename__ = "books"

    book_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    book_title = db.Column(db.String)
    author_name = db.Column(db.String)
    publish_date = db.Column(db.String)
    book_image = db.Column(db.String)

    favorites = db.relationship("Favorite", back_populates="book")
    bookgenre = db.relationship("BookGenre", back_populates="book")

    def as_dict(self):
        """source: https://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return f"<Book book_id={self.book_id} book_title={self.book_title} author_name={self.author_name}>"


class Favorite(db.Model):
    """A favorited book."""

    __tablename__ = "favorites"

    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), primary_key = True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.book_id"), primary_key = True)

    # source: https://medium.com/@thinesh12/unlocking-the-power-of-composite-primary-keys-in-sqlalchemy-b378fb975e9b
    __table_args__ = ( PrimaryKeyConstraint('user_id', 'book_id'),)

    user = db.relationship("User", back_populates="favorites")
    book = db.relationship("Book", back_populates="favorites")

    def __repr__(self):
        return f"<Favorite book_id={self.book_id} user_id={self.user_id}>"


class BookGenre(db.Model):
    """A middle table for book and genre."""

    __tablename__ = "bookgenre"

    bookgenre_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.book_id"))
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.genre_id"))
    # genre_name = db.Column(db.String)


    book = db.relationship("Book", back_populates="bookgenre")
    genre = db.relationship("Genre", back_populates="bookgenre")

    def __repr__(self):
        return f"<BookGenre bookgenre_id={self.bookgenre_id}>"

class Genre(db.Model):
    """A middle table for book and genre."""

    __tablename__ = "genres"

    genre_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    genre_name = db.Column(db.String)
    is_fiction = db.Column(db.Boolean)


    bookgenre = db.relationship("BookGenre", back_populates="genre")

    def __repr__(self):
        return f"<Genre genre_id={self.genre_id}>"



def connect_to_db(flask_app, db_uri="postgresql:///books", echo=True):
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