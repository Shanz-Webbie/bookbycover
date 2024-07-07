from flask import Flask, render_template, request, redirect, flash, session, abort
from model import User, connect_to_db, db
import crud
from jinja2 import StrictUndefined


from pprint import pformat
import os


app = Flask(__name__)

# ToDo remove secret and config from global scope

app.secret_key = 'SECRETSECRETSECRET'

# This configuration option makes the Flask interactive debugger
# more useful (you should remove this line in production though)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True
app.jinja_env.undefined = StrictUndefined

def get_user_from_session() -> User | None:
    user_email = session.get("user_email")
    if user_email:
        return crud.get_user_by_email()
    else:
        return None


def get_api_key():
    API_Key = os.environ['GOOGLEBOOKS_KEY']
    return API_Key


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

@app.route("/signup", methods=["POST", "GET"])
def register_user():
    """Create a new user."""

    user_email = request.form.get("user_email")
    user_password = request.form.get("user_password")
    user_first_name = request.form.get("user_first_name")
    user = crud.get_user_by_email(user_email)
    if user:
        flash("Email already in use. Try again.")
        return abort(400)
    else:
        user = crud.create_user(user_email, user_password, user_first_name)
        flash("Account created! Please log in.")
        return redirect("/browse")





@app.route("/login")
def show_login_page():
    """Show login page."""
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    user_email = request.form.get("user_email")
    password = request.form.get("user_password")

    # if request.method == "POST":
    #     session.permanent = True
    #     session["user_email"] = user_email


    # user = crud.get_user_by_email(user_email)
    # if not user or user.user_password != password:
    #     flash("The email or password you entered was incorrect.")
    # else:
    #     # Log in user by storing the user's email in session
    #     session["user_email"] = user.user_email
    #     flash(f"Welcome back, {user.user_email}!")

    # return redirect("/browse")

@app.route('/browse')
def browse():
    """Show browsing homepage."""

    return render_template('browse.html')

@app.route('/favorites')
def favorites():
    """Show favorites homepage."""

    return render_template('favorites.html')

@app.route('/login', methods=["POST"])
def login():
    """Get username and password"""

    # user = crud.get_user_by_email(session['email'])

    # user_login_info = crud.create_user(user)

    # if verify_authorization(user):
    #     return redirect("/home")

    # db.session.add(user_login_info)
    # db.session.commit()

    return render_template('login.html')

if __name__ == '__main__':
    connect_to_db(app)
    app.debug = True
    # loopback address
    app.run(host='0.0.0.0', port=6060)