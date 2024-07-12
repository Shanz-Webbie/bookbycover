
// const searchInput = document.getElementById('bookSearch');
// const searchButton = document.getElementById('searchButton');

// searchButton.addEventListener('click', function(){
//     const searchQuery = searchInput.value;
//     console.log(`Searching for '${searchQuery}'...`);

// });

function showBook(evt) {
    evt.preventDefault();
    const url = '/books.json';
    // const requestedBooks = new Request("books.json")
    const book_title = document.querySelector('#title-field').value;
    console.log('Success!')
    fetch(`/books.json?title=${book_title}`)
        .then((response) => response.json())
        .then((searchedBooks) => {
            console.log(searchedBooks)
            const searchResultsDiv = document.querySelector('#search-results');
            searchedBooks.forEach(book => {
                console.log(book)
                searchResultsDiv.innerHTML = `<h2>Search Results:</h2><h3>${book.book_title}</h3><p>${book.author_name}</p><p><img class="poster" src='${book.book_image}'/></p>`;

            });


        });
}

    document.querySelector('#title-form').addEventListener('submit', showBook);


function addFavorites(evt){
    // To Do : add "not implemented" alert
    console.log("Test")
    evt.preventDefault();
    // fetch('/browse/<book_id>/favorite')

}

    document.querySelector('#favorite-button').addEventListener('click', addFavorites);
