import requests

# source: https://www.youtube.com/watch?v=fsB8_79zI_A
# arjan code design patterns adapters

class BookAdapter:

    """A Google Book adapter that uses the requests library."""

    def get_books_by_title(self, title: str) -> list[dict]:
        # source: https://developers.google.com/books/docs/v1/using
        url = "https://www.googleapis.com/books/v1/volumes"
        payload = { 'q': (f"{title}+intitle:{title}") }

        response = requests.get(url, params=payload)
        response_dict = response.json()
        return response_dict