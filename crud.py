"""CRUD operations"""

from model import db, User, Book, BookGenre, Genre, Favorite, connect_to_db

def create_user(user_email,user_password,user_first_name):
    """Create and return a new user."""
    user = User(user_email=user_email, user_password=user_password, user_first_name= user_first_name)

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

    return User.query.filter(User.user_email == email).first()

def create_book(book_title, author_name, publish_date, genre_name, is_fiction, book_image):
    """Create and return a book."""
    book = Book(
        book_title = book_title,
        author_name = author_name,
        publish_date = publish_date,
        book_image = book_image
    )
    genre = Genre(
        genre_name= genre_name,
        is_fiction= is_fiction
    )

    book_genre = BookGenre(
        book_id= book.book_id,
        genre_id = genre.genre_id

    )

    db.session.add(book)
    db.session.add(genre)
    db.session.add(book_genre)
    db.session.commit()

    return book

def get_books():
    """Return all books."""

    return Book.query.all()

def get_favoties():
    """Return all favories."""

    return Favorite.query.all()


def get_book_by_id(book_id):
    """Return a book by primary key."""

    return Book.query.get(book_id)

def get_genres(genre_name):
    """Return all book genres."""

    return Genre.query.all(genre_name)

def get_genre_by_id(genre_id):
    """Return a genre by primary key."""

    return Genre.query.get(genre_id)

def create_favorite(user: User, book: Book) -> Favorite:
    """Create and return a favorited book object."""

    favorite_obj = Favorite(user=user, book=book)

    db.session.add(favorite_obj)
    db.session.commit()

    return favorite_obj

def get_favorite_by_id(favorite_id):
    """Return a favorite by primary key."""

    return Favorite.query.get(favorite_id)

def delete_a_favorite(user: User, book: Book) -> Favorite:
    """ Delete a favorite. """
    deleted_favorite_obj = Favorite(user=user, book=book)
    db.session.delete(deleted_favorite_obj)
    db.session.commit()

def delete_a_book(book):
    """ Delete a book. """
    db.session.delete(book)
    db.session.commit()

def delete_a_user(user):
    """ Delete a user. """
    db.session.delete(user)
    db.session.commit()

if __name__ == "__main__":
    from server import app

    connect_to_db(app)