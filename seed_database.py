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

# Use fake book data from JSON until API is implemented
with open("data/books.json") as f:
    book_data = json.loads(f.read())

books_in_db = []
for book in book_data:
    title, author_name, publish_date, genre_name, is_fiction = (
         book["title"],
        book["author"],
        book["publish_date"],
        book["genre_name"],
        book["is_fiction"]
    )

    db_book = crud.create_book(title, author_name, publish_date, genre_name, is_fiction)
    books_in_db.append(db_book)

db.session.add_all(books_in_db)
db.session.commit()
