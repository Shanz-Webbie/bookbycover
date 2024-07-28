import requests
from book_marshaller import BookMarshaller
from model import Book
from server import get_api_key
from abc import abstractmethod , ABC

# source: https://www.youtube.com/watch?v=fsB8_79zI_A
# arjan code design patterns adapters

class AbstractBookAdapter(ABC):
    @abstractmethod
    def get_books_by_title(self, title: str) -> dict:
        """Get book by title and return dict."""


class BookAdapter(AbstractBookAdapter):

    """A Google Book adapter that uses the requests library."""

    def get_books_by_title(self, title: str) -> dict:
        # source: https://developers.google.com/books/docs/v1/using
        url = "https://www.googleapis.com/books/v1/volumes"
        payload = { 'q': (f"{title}+intitle:{title}") }

        response = requests.get(url, params=payload)
        response_dict = response.json()
        return response_dict

class BookFacade:
    # source: https://python-dependency-injector.ets-labs.org/introduction/di_in_python.html
    # source: https://www.youtube.com/watch?v=2ejbLVkCndI
    # arjan codes "Dependency INVERSION vs Dependency INJECTION in Python"

    adapter: AbstractBookAdapter
    def __init__(self, adapter: AbstractBookAdapter):
        self.adapter = adapter

    def convert_book_dict(self, title: str) -> list[Book]:
        book_marshaller = BookMarshaller()
        response_dict_result = self.adapter.get_books_by_title(title)
        converted_books = []
        for book_dict in response_dict_result["items"]:
            marshalled_book = book_marshaller.marshall(book_dict)
            converted_books.append(marshalled_book)
        return converted_books


def main(title):
    googlebooks_api = get_api_key(api_key= None)
    lists_books = googlebooks_api.get_books_by_title(title= title)
    print(lists_books)


if __name__ == '__main__':
    main()