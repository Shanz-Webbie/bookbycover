# BookByCover
## _Personalized book browsing platform_

[Link to the live demo](https://songstratus.herokuapp.com/)

<img src="https://media.istockphoto.com/id/1313502372/vector/book-icon-open-pages-education-symbol-book-black-silhouette.jpg?s=612x612&w=0&k=20&c=0occ552bX8hSKR9h2upiaEwlNnlpufs2trCqk0j-RXc="/>


BookByCover is a mobile-responsive web application that allows users to browse and favorite books, powered by the Google Books API. It also supports offline storage for seamless access anytime, anywhere.

# Login or register an account
<img src="https://i.imgur.com/57Ino1c.png"/>
Our book browsing app offers a seamless and intuitive user onboarding experience, ensuring you can quickly dive into exploring your next great read. When signing up, new users are prompted to create a personalized account by entering their username, password, and first name. This straightforward process ensures that your experience is tailored from the very start.

Once the required information is entered, users are automatically redirected to the login page. Here, you can securely enter your newly created credentials and immediately begin discovering, browsing, and saving your favorite books. This smooth transition from sign-up to sign-in ensures a hassle-free start to your book browsing journey.

# Search by title or author
<img src="https://i.imgur.com/od2VSGJ.png"/>
BookByCover empowers you to find exactly what you're looking for with an advanced search feature that allows you to search by book title or author. Whether you're looking for a specific book or exploring an author's entire collection, our search function delivers results.

Every search result is automatically saved, allowing you to revisit your searches at any time. This ensures that no book you’re interested in is lost in the shuffle.


# Browse books
<img src="https://i.imgur.com/BR3FVVa.png"/>

As you explore our browse page, you can easily manage your personal library by saving or deleting your favorite books with just a tap. Keep track of the titles you love, and curate a collection that reflects your unique tastes. With these powerful tools at your fingertips, discovering, organizing, and enjoying books has never been easier.

# Save or delete a favorite book
<img src="https://i.imgur.com/ntw6l8P.png"/>

When you navigate to the favorites page, you'll find all the books you've saved neatly organized for easy viewing. Here, you can add new favorites or remove any that no longer capture your interest, giving you complete control over your personal collection.

And if you haven’t saved any favorites yet, don’t worry! The favorites page will display a friendly message encouraging you to explore the library and start building your collection.

✨Magic ✨

## GitHub


The GitHub repository for BookByCover hosts the complete source code for a dynamic, mobile-responsive web application that leverages the Google Books API for seamless book browsing and favoriting with an intuitive user interface.

[BookByCover GitHub](https://github.com/Shanz-Webbie/bookbycover)

## Features

- Mobile-Responsive Design: Optimized for use on smartphones, tablets, and desktops.
- Google Books API Integration: Search and explore a vast collection of books directly from the Google Books database.
- Offline Storage: Save favorite books locally for access without an internet connection.
- Book Favoriting: Easily mark and organize your favorite books for quick reference.
- Search by Title and Author: Quickly find books using intuitive search functionality.
- User-Friendly Interface: Clean and easy-to-navigate interface for an enhanced browsing experience.
- Fast Loading Times: Efficiently loads book data, ensuring a smooth user experience.
- Cross-Platform Compatibility: Accessible across different devices and operating systems.


> Discover a world of literature tailored just for you with our personalized book browsing platform. Powered by the Google Books API, BookByCover curates a diverse selection of literary treasures at your fingertips.  Filter through libraries by author or title to uncover your next great read. Save your favorite books for later, and manage your collection by removing titles once you've finished them. All your preferences and saved selections are securely tied to your personal account, ensuring a unique and customized browsing experience every time.



## Tech

BookByCover uses a number of languages and libraries to work:

- [Flask] - Routing, request handling, and templating
- [SQL Alchemy] - ORM
- [Requests] - HTTP request handler
- [ABC] - Abstract Base Class for consistent structure in OOP
- [BootStrap](https://getbootstrap.com/) - Ready made frontend design for repsonsive pages across different devices


## Installation

BookByCover requires [Python](https://www.python.org/downloads/) v3+ and [Google Books API](https://developers.google.com/books) to run.

Sign up for Google Books API. Quickstart guide [here](https://developers.google.com/books/docs/v1/getting_started).

Install the dependencies and start the server.

For production environments...

```sh
pip3 install -r requirements.txt
```

## Port Addressing

By default, the server will use port 6060, so change this within the
server file if necessary.


Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:6060
10.0.0.247:6060/
```


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [Flask]: <https://flask.palletsprojects.com/en/3.0.x/installation/>
   [SQL Alchemy]: <https://www.sqlalchemy.org/>
   [Requests]: <https://pypi.org/project/requests/>
   [ABC]: <https://docs.python.org/3/library/abc.html>
