from flask import Flask, render_template, request, redirect, flash, session

from pprint import pformat
import os


app = Flask(__name__)
app.secret_key = 'SECRETSECRETSECRET'

# This configuration option makes the Flask interactive debugger
# more useful (you should remove this line in production though)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True

API_Key = os.environ['GOOGLEBOOKS_KEY']

@app.route('/')
def homepage():
    """Show homepage."""

    return render_template('homepage.html')

def verify_authorization(username, password):
    """Verify if user is authorized."""

    authorized = False
    if username and password:
        authorized = True
    return authorized

@app.route('/', methods=["POST", "GET"])
def login():
    """Get username and password"""

    username = request.form.get("username")
    password = request.form.get("password")
    if verify_authorization(username, password):
        return redirect("/home")
    return render_template('login.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=6060)