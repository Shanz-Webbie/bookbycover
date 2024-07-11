import json
from flask import Flask, render_template, request, redirect, flash, session, abort, jsonify
from model import User, connect_to_db, db
import crud
from jinja2 import StrictUndefined



from pprint import pformat
import os



app = Flask(__name__)

# ToDo remove secret and config from global scope

def get_api_key():
    API_Key = os.environ['GOOGLEBOOKS_KEY']
    return API_Key

app.secret_key = get_api_key()

# with open('data/books.json', 'r') as json_file:
#     books_data = json.load(json_file)

# books = books_data['books']

# This configuration option makes the Flask interactive debugger
# more useful (you should remove this line in production though)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True
app.jinja_env.undefined = StrictUndefined

def get_user_from_session() -> User | None:
    user_email = session.get("user_email")
    if user_email:
        return crud.get_user_by_email(user_email)
    else:
        return None



def is_user_authorized() -> bool:
    """Verify if user is authorized."""

    user = get_user_from_session()
    if user:
        return True
    else:
        return False

@app.route('/')
def homepage():
    """Show homepage."""
    # if user in session
        # return redirect "browse"
    # else return redirect "login"

    if is_user_authorized():
        return redirect("/browse")
    else:
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


    if is_user_authorized():
        return redirect("/browse")
    if not user:
        return redirect("/signup")
    if user.user_password == user_password:
        user = crud.get_user_by_email(user_email)
        session["user_email"] = user_email
        flash("Success!")
        return redirect("/browse")
    else:
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

    return render_template('favorites.html')

@app.route('/books.json')
def get_book_by_title():
    """Return a book-info dictionary for this title."""
    # open the JSON file
    with open('data/books.json') as json_file:
        json_data = json.load(json_file)
        # get the input title from the search bar
    title = request.args.get('title-field')
    # iterate over each book in the JSON file
    for book in json_data:
        # if the book title matches what was input
        if book.get('title') == title:
            title_info = book
            break

    return jsonify([title_info])

    #     json_data = json.loads(json_file.read())
    # return(render_template("browse.html", jsonify_data=jsonify_data))



@app.route('/browse')
def search_books():
    """Search and display relevant books."""
    # get the input title from the search bar
    # title = request.args.get('title')
    # found_books = [book for book in books if title in book['title']]
    # return render_template('browse.html', books=found_books)
#     # json_file = open('data/books.json')
#     # json_data = json_file.read()
#     # json_obj = json.loads(json_data)
#     # json_str = json.dumps(json_obj)
#     # return json_str
#     # dict_obj = {"hello": "world"}
#     # json_str = json.dumps(dict_obj)
#     # return json_str

@app.route("/browse/<book_id>/favorite", methods=["POST"])
def create_favorite(book_id):
    """Create a new favorite book."""
    logged_in_email = session.get("user_email")
    is_favorite = request.form.get("favorite-button")
    if is_user_authorized:
        user = crud.get_user_by_email(logged_in_email)
        book = crud.get_book_by_id(book_id)

        favorite = crud.create_favorite(user, book, is_favorite)
        db.session.add(favorite)
        db.session.commit()

        flash(f"Saved the favorite.")
    return redirect(f"/browse/{book_id}")


if __name__ == '__main__':
    connect_to_db(app)
    app.debug = True
    # loopback address
    app.run(host='0.0.0.0', port=6060)