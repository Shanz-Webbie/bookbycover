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

def get_user_by_email(email: str) -> User:
    """Return a user by email."""

    return User.query.filter(User.user_email == email).first()


def duplicate_books(book_to_check: Book) -> list[Book]:
    """Check for matching books in the database."""
    # get all books from database
    db_books = get_books()
    matching_books = [
        book for book in db_books if
        book.book_title == book_to_check.book_title and
        book.author_name == book_to_check.author_name
        and book.publish_date == book_to_check.publish_date
    ]
    return matching_books

def safely_add_unique_book(book: Book):
    try:
        if duplicate_books(book):
            raise Exception("This book is already in the database.")
    except Exception as error:
        print(f"Error with adding book: {error}")
    db.session.add(book)
    db.session.commit()

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

    safely_add_unique_book(book)
    db.session.add(genre)
    db.session.add(book_genre)
    db.session.commit()

    return book


def add_books_to_database(list_of_books: list[Book]):
    """Add books from the facade to the database."""

    for book in list_of_books:
        safely_add_unique_book(book)


def get_books():
    """Return all books."""

    return Book.query.all()

def get_favorite_books_for_a_given_user(user: User) -> list[Book]:
    """Return a given users favorite books."""
    matching_favorites = Favorite.query.filter(Favorite.user_id == user.user_id).all()
    book_ids_of_matched_favorites = [favorite.book_id for favorite in matching_favorites]
    books_that_match_a_given_book_id = Book.query.filter(Book.book_id.in_(book_ids_of_matched_favorites)).all()
    return books_that_match_a_given_book_id


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


def get_favorite_by_book_id(book_id, user_id):
    """Return a favorite by book id."""

    return Favorite.query.filter_by(book_id=book_id, user_id=user_id).first()

def delete_favorite(favorite: Favorite):
    """ Delete a favorite. """
    db.session.delete(favorite)
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