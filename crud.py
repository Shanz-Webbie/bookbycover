"""CRUD operations"""

from model import db, User, Book, BookGenre, Genre, Favorite

def create_user(email,password,first_name,last_name):
    """Create and return a new user."""
    user = User(email=email, password=password, first_name= first_name, last_name=last_name)

    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    """Return all users."""

    return User.query_all()

def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def create_book(title, author, publish_date, book_image):
    """Create and return a book."""
    book = Book(
        title = title,
        author = author,
        publish_date = publish_date,
        book_image = book_image
    )

    db.session.add(book)
    db.session.commit()

    return book

def get_books():
    """Return all books."""

    return Book.query.all()

def get_book_by_id(book_id):
    """Return a book by primary key."""

    return Book.query.get(book_id)

def get_genres(genre_name):
    """Return all book genres."""

    return Genre.query.all(genre_name)

def get_genre_by_id(genre_id):
    """Return a genre by primary key."""

    return Genre.query.get(genre_id)

def create_favorite(user, book):
    """Create and return a favorited book object."""

    favorite_obj = Favorite(user=user, book=book)

    db.session.add(favorite_obj)
    db.session.commit()

    return favorite_obj

def get_favorite_by_id(favorite_id):
    """Return a favorite by primary key."""

    return Favorite.query.get(favorite_id)

def delete_a_favorite(favorite):
    """ Delete a favorite. """
    db.session.delete(favorite)