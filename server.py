from flask import Flask, render_template, request, redirect, flash, session
from model import connect_to_db, db
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

def get_api_key():
    API_Key = os.environ['GOOGLEBOOKS_KEY']
    return API_Key

@app.route('/')
def homepage():
    """Show homepage."""

    return render_template('homepage.html')

# def verify_authorization(user):
#     """Verify if user is authorized."""

#     authorized = False
#     if user:
#         authorized = True
#     return authorized

@app.route("/signup", methods=["POST"])
def register_user():
    """Create a new user."""

    user_email = request.form.get("email")
    password = request.form.get("password")
    first_name = request.form.get("fname")

    user = crud.get_user_by_email(user_email)
    if user:
        flash("Email already in use. Try again.")
    else:
        user = crud.create_user(user_email, password, first_name)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/browse")

@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.user_password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.user_email
        flash(f"Welcome back, {user.user_email}!")

    return redirect("/browse")

@app.route('/browse')
def browse():
    """Show browsing homepage."""

    return render_template('browse.html')

@app.route('/favorites')
def favorites():
    """Show favorites homepage."""

    return render_template('favorites.html')

# @app.route('/login', methods=["POST"])
# def login():
#     """Get username and password"""

#     # user = crud.get_user_by_email(session['email'])

#     # user_login_info = crud.create_user(user)

#     # if verify_authorization(user):
#     #     return redirect("/home")

#     # db.session.add(user_login_info)
#     # db.session.commit()

#     return render_template('login.html')

if __name__ == '__main__':
    connect_to_db(app)
    app.debug = True
    # loopback address
    app.run(host='0.0.0.0', port=6060)