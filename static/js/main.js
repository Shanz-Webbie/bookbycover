function showBookByTitle(evt) {
  evt.preventDefault();
  const url = "/books.json";
  // const requestedBooks = new Request("books.json")
  const book_title = document.querySelector("#title-field").value;
  console.log("Success!");
  fetch(`/books/search/title?title=${book_title}`)
    .then((response) => response.json())
    .then((searchedBooks) => {
      console.log(searchedBooks);
      const searchResultsDiv = document.querySelector("#search-results");
      // source: https://www.sitepoint.com/loop-through-json-response-javascript/
      searchResultsDiv.innerHTML = `<h3>Search Results:</h3>`
      searchedBooks.forEach((book) => {
        console.log(book);
        // source: https://www.digitalocean.com/community/tutorials/how-to-add-javascript-to-html
        // https://www.geeksforgeeks.org/how-to-append-html-code-to-a-div-using-javascript/

        searchResultsDiv.innerHTML += `<h1>${book.book_title}</h1>
        <h2>${book.author_name}</h2>
        <p><img class="poster" src='${book.book_image}'/></p>`;
      });
    });
}

function showBookByAuthor(evt) {
  evt.preventDefault();
  const author_name = document.querySelector("#author-field").value;
  console.log("Success!");

  fetch(`/books/search/author?author=${author_name}`)
    .then((response) => response.json())
    .then((searchedBooks) => {
      const searchResultsDiv = document.querySelector("#search-results");
      // source: https://www.sitepoint.com/loop-through-json-response-javascript/
      searchResultsDiv.innerHTML = `<h3>Search Results:</h3>`
      searchedBooks.forEach((book) => {
        console.log(book);
        // source: https://www.digitalocean.com/community/tutorials/how-to-add-javascript-to-html
        // https://www.geeksforgeeks.org/how-to-append-html-code-to-a-div-using-javascript/
        searchResultsDiv.innerHTML += `<h1>${book.book_title}</h1>
        <h2>${book.author_name}</h2>
        <p><img class="poster" src='${book.book_image}'/></p>`;
      });
    });
}





function addFavorite(evt) {
  // To Do : add "not implemented" alert
  alert("Favorite saved");
  // source: https://stackoverflow.com/questions/7822407/why-is-my-alert-showing-more-than-once
  evt.stopImmediatePropagation();
  const favButton = evt.target;
  const book_id = favButton.dataset.bookId;
  console.log(`book id is: ${book_id}`);
  // source: https://stackoverflow.com/questions/38235715/fetch-reject-promise-and-catch-the-error-if-status-is-not-ok
  fetch(`/favorites/${book_id}`, {
    method: "POST",
  })
    .then((response) => {
      console.log("response received");
      if (!response.ok) {
        throw new Error("Something went wrong");
      }
    })
    .catch((error) => {
      console.log(error);
    });
}


function removeFavorite(evt) {
  alert("Favorite removed");
  // source: https://stackoverflow.com/questions/7822407/why-is-my-alert-showing-more-than-once
  evt.stopImmediatePropagation();
  const delFavButton = evt.target;
  const book_id = delFavButton.dataset.bookId;

  fetch(`/favorites/${book_id}/delete`, {
    method: "DELETE",
  })
    .then((response) => {
      console.log("response received");
      if (!response.ok) {
        throw new Error("Something went wrong");
      }
      // Remove the book item from the DOM
      const deletedBookItem = delFavButton.closest(".container");
      if (deletedBookItem) {
        deletedBookItem.remove();
      }
    })
    .catch((error) => {
      console.log(error);
    });
}



// source: https://developer.mozilla.org/en-US/docs/Web/API/Document/DOMContentLoaded_event
document.addEventListener("DOMContentLoaded", () => {
  // source: https://stackoverflow.com/questions/12330086/how-to-loop-through-selected-elements-with-document-queryselectorall
  document.querySelectorAll(".favorite-button").forEach((button) => {
    button.addEventListener("click", addFavorite);
  });

  document.querySelectorAll(".del-favorite-button").forEach((button) => {
    button.addEventListener("click", removeFavorite);
  });

  document.querySelectorAll(".del-favorite-button-fav-page").forEach((button) => {
      console.log("Delete");
      button.addEventListener("click", removeFavorite, setTimeout);
    });
});

// // source: https://www.basedash.com/blog/how-to-create-a-toggle-button-in-javascript

// source: https://stackoverflow.com/questions/49961201/javascript-alert-when-no-matching-results-from-search-query

browsePageForm = document.querySelector("#title-form")

if (browsePageForm){
    browsePageForm.addEventListener("submit", showBookByTitle);
}

browsePageFormAuthor = document.querySelector("#author-form")

if (browsePageForm){
    browsePageFormAuthor.addEventListener("submit", showBookByAuthor);
}
