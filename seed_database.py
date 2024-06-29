import os
#ToDo add API file
import json

import crud
from model import connect_to_db, db
from server import app

os.system("dropdb books")
os.system("createdb books")

connect_to_db(app)
app.app_context().push()
db.create_all()
