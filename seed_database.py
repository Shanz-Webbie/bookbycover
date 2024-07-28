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

# add in additional data via loop to delete
books_in_db = []
# for book in API limit 100
for book in book_data:
    book_title, author_name, publish_date, genre_name, is_fiction, book_image = (
        book["book_title"],
        book["author_name"],
        book["publish_date"],
        book["genre_name"],
        book["is_fiction"],
        book["book_image"],
    )

    db_book = crud.create_book(book_title, author_name, publish_date, genre_name, is_fiction, book_image)
    books_in_db.append(db_book)

db.session.add_all(books_in_db)
db.session.commit()
