import json
from flask import Flask, Response, render_template, request, redirect, flash, session, abort, jsonify
from book_marshaller import BookMarshaller
from googlebooks import BookAdapter, BookFacade, build_adapter
from model import User, Book, connect_to_db, db
import crud
import requests
from jinja2 import StrictUndefined
import logging


from pprint import pformat
import os

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

def get_session_secret():
    return "SECRETSECRETSECRET"

app.secret_key = get_session_secret()

# # This configuration option makes the Flask interactive debugger
# # more useful (you should remove this line in production though)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True
app.jinja_env.undefined = StrictUndefined

def get_user_from_session() -> User | None:
    user_email = session.get("user_email")
    if user_email:
        return crud.get_user_by_email(user_email)
    else:
        return None



@app.route('/')
def homepage():

    if get_user_from_session():
        return redirect("/browse")
    return redirect("/login")


@app.route("/signup")
def show_signup_page():
    """Show signup page."""
    return render_template("signup.html")

@app.route("/signup", methods=["POST", "GET"])
def register_user():
    """Create a new user."""

    user_email = request.form.get("user_email")
    user_password = request.form.get("user_password")
    user_first_name = request.form.get("user_first_name")
    if crud.get_user_by_email(user_email):
        flash("Email already in use. Try using a different password.")
        return redirect("/login")
        # return abort(400)
    else:
        user = crud.create_user(user_email, user_password, user_first_name)
        flash("Account created!")
        return redirect("/login")


@app.route("/login")
def show_login_page():
    """Show login page."""
    return render_template("login.html")


@app.route("/login", methods=["POST", "GET"])
def process_login():
    """Process user login."""

    user_email = request.form.get("user_email")
    user_password = request.form.get("user_password")
    user = crud.get_user_by_email(user_email)

# edge: user is logged in but not the same user

    if get_user_from_session():
        return redirect("/browse")
    if not user:
        return redirect("/signup")
    if user.user_password == user_password:
        user = crud.get_user_by_email(user_email)
        session["user_email"] = user_email
        flash("Success!")
        return redirect("/browse")
    else:
        # source: https://flask.palletsprojects.com/en/3.0.x/errorhandling/
        flash("The email or password you entered was incorrect.")
        return abort(400)

@app.route('/browse')
def browse():
    """Show browsing homepage."""

    user_object = get_user_from_session()
    flash(f"Welcome back, {user_object.user_first_name}!")
    books = crud.get_books()
    return render_template('browse.html', user_first_name=user_object.user_first_name, books=books)

@app.route('/favorites')
def favorites():
    """Show favorites homepage."""
    user = get_user_from_session()
    if not user:
        return Response(status=401)
    favorites = crud.get_favorite_books_for_a_given_user(user)
    return render_template('favorites.html', favorites=favorites)


@app.route('/books/search/title', methods=["POST", "GET"])
def get_book_by_title():
    """Return a book-info dictionary for this title."""

    adapter = build_adapter()
    marshaller = BookMarshaller()
    book_facade = BookFacade(adapter, marshaller)

    # get searched title from form
    title = request.args.get("title")
    # authors = request.args.get("author")
    recieved_data = book_facade.receive_and_convert_books_title(title)
    crud.add_books_to_database(recieved_data)

    # GoogleBooks: title, authors, imageLinks (thumbnail)
    # maxResults - The maximum number of results to return. The default is 10, and the maximum allowable value is 40.



    # query the database for books with a matching title
    # source: https://www.geeksforgeeks.org/postgresql-ilike-operator/
    db_books: list[Book] = Book.query.filter(Book.book_title.ilike(f"%{title}%")).limit(20).all()
    # convert all the db books into a dictionary
    matching_books_dict = [book.as_dict() for book in db_books]



    return jsonify(matching_books_dict)

@app.route('/books/search/author', methods=["POST", "GET"])
def get_book_by_author():
    """Return a book-info dictionary for this author."""

    adapter = build_adapter()
    marshaller = BookMarshaller()
    book_facade = BookFacade(adapter, marshaller)

    # get searched title from form
    author = request.args.get("author")
    # authors = request.args.get("author")
    recieved_data = book_facade.receive_and_convert_books_author(author)
    crud.add_books_to_database(recieved_data)

    # GoogleBooks: title, authors, imageLinks (thumbnail)
    # maxResults - The maximum number of results to return. The default is 10, and the maximum allowable value is 40.



    # query the database for books with a matching title
    # source: https://www.geeksforgeeks.org/postgresql-ilike-operator/
    db_books: list[Book] = Book.query.filter(Book.author_name == author).limit(20).all()
    # convert all the db books into a dictionary
    matching_books_dict = [book.as_dict() for book in db_books]



    return jsonify(matching_books_dict)

@app.route("/favorites/<book_id>", methods=["POST"])
def create_a_favorite(book_id: int):
    user = get_user_from_session()
    if user:
        book = crud.get_book_by_id(book_id)
        favorite = crud.create_favorite(user=user, book=book)
        db.session.add(favorite)
        db.session.commit()
        return Response(status=200)
    else:
        raise NotImplementedError

@app.route("/favorites/<book_id>/delete", methods=["DELETE"])
# edge: if favorite id is incorrect or favorite user id doesn't match
def delete_a_favorite(book_id: int):
    user = get_user_from_session()
    if user:
        favorite = crud.get_favorite_by_book_id(book_id, user_id= user.user_id)
        if favorite:
            crud.delete_favorite(favorite)
        # source: https://stackoverflow.com/questions/24295426/python-flask-intentional-empty-response
        return Response(status=204)
    else:
        raise NotImplementedError



if __name__ == '__main__':
    connect_to_db(app)
    app.debug = True
    # loopback address
    app.run(host='0.0.0.0', port=6060)