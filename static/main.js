
// const searchInput = document.getElementById('bookSearch');
// const searchButton = document.getElementById('searchButton');

// searchButton.addEventListener('click', function(){
//     const searchQuery = searchInput.value;
//     console.log(`Searching for '${searchQuery}'...`);

// });

function showBook(evt) {
    evt.preventDefault();
    const url = '/books.json';
    const book_title = document.querySelector('#title-field').value;
    console.log('Success!')
    fetch(`/books.json?${book_title}`)
        .then((response) => response.text())
        .then((title) => {
            document.querySelector('#search-results').innerHTML = title});
}

document.querySelector('#title-form').addEventListener('submit', showBook);