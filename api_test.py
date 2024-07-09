from server import get_api_key
import requests

def main():
    api_key = get_api_key()
    response = requests.get("https://www.googleapis.com/books/v1/volumes?q=harry+potter")
    print(response.json())

if __name__ == '__main__':
    main()