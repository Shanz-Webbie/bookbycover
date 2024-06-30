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

def verify_authorization(user):
    """Verify if user is authorized."""

    authorized = False
    if user:
        authorized = True
    return authorized

@app.route('/home', methods=["POST", "GET"])
def login():
    """Get username and password"""

    user = crud.get_user_by_email(session['email'])

    user_login_info = crud.create_user(user)

    if verify_authorization(user):
        return redirect("/home")

    db.session.add(user_login_info)
    db.session.commit()

    return render_template('login.html')

if __name__ == '__main__':
    connect_to_db(app)
    app.debug = True
    # loopback address
    app.run(host='127.0.0.1', port=6060)