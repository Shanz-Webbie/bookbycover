from model import Book
from abc import abstractmethod, ABC

class AbstractBookMarshaller(ABC):
    @abstractmethod
    def marshall(self, book_dict: dict) -> Book:
        """Get dictionary of books and convert to Book objects."""

class BookMarshaller(AbstractBookMarshaller):
    def marshall(self, book_dict: dict) -> Book:
        # volumeInfo is the GoogleBooks key
        volume_info = book_dict.get("volumeInfo", {})
        title = volume_info.get("title")
        authors = volume_info.get("authors")
        # thumbnail is nested in imageLinks
        imageLinks = volume_info("imageLinks", {}).get("thumbnail")
        return Book(title= title, authors= authors, imageLinks=imageLinks)