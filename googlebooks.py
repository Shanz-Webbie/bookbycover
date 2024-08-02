import os
import requests
from book_marshaller import AbstractBookMarshaller, BookMarshaller
from model import Book
from abc import abstractmethod , ABC

def get_api_key():
    API_Key = os.getenv('GOOGLEBOOKS_KEY')
    return API_Key

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
        # ToDo : Add API key to payload
        url = "https://www.googleapis.com/books/v1/volumes"
        payload = { 'q': (f"{title}+intitle:{title}"),
                    'key': get_api_key(),
                    }

        response = requests.get(url, params=payload)
        response_dict = response.json()
        return response_dict

class BookFacade():
    # source: https://python-dependency-injector.ets-labs.org/introduction/di_in_python.html
    # source: https://www.youtube.com/watch?v=2ejbLVkCndI
    # source: https://medium.com/@amirm.lavasani/design-patterns-in-python-facade-0043afc9aa4a
    # arjan codes "Dependency INVERSION vs Dependency INJECTION in Python"

    adapter: AbstractBookAdapter
    marshaller: AbstractBookMarshaller
    def __init__(self, adapter: AbstractBookAdapter, marshall: AbstractBookMarshaller):
        self.adapter = adapter
        self.marshaller = marshall

    def receive_and_convert_books(self, title: str) -> list[Book]:
        response_dict_result = self.adapter.get_books_by_title(title)
        converted_books = self.marshaller.marshall(response_dict_result)
        return converted_books

def build_adapter() -> AbstractBookAdapter:
    return BookAdapter()

def main(title):
    googlebooks_api = get_api_key(api_key= None)
    lists_books = googlebooks_api.get_books_by_title(title= title)
    print(lists_books)


if __name__ == '__main__':
    main()
