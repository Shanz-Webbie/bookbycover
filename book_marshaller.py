from model import Book
from abc import abstractmethod, ABC

class AbstractBookMarshaller(ABC):
    @abstractmethod
    def marshall(self, response_book_dict: dict) -> list[Book]:
        """Get dictionary of books and convert to Book objects."""


class BookMarshaller(AbstractBookMarshaller):
    def marshall(self, response_dict_result: dict) -> list[Book]:
        converted_books = []
        try:
            items = response_dict_result["items"]
        except KeyError:
            raise RuntimeError("Rate limit exceeded")
        for book_dict in items:
            # volumeInfo is the GoogleBooks key
            volume_info = book_dict.get("volumeInfo", {})
            title = volume_info.get("title")
            authors = volume_info.get("authors", [])
            publishedDate = volume_info.get("publishedDate")
            # thumbnail is nested in imageLinks
            imageLinks = volume_info.get("imageLinks", {}).get("thumbnail")
            # only display the first author for formatting consistency
            if authors:
            # only display books with an image
                first_author = authors[0]
            if imageLinks:
                marshalled_book = Book(book_title= title, author_name= first_author, publish_date= publishedDate, book_image=imageLinks)
            converted_books.append(marshalled_book)
        return converted_books

