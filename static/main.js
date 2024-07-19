
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
            // source: https://www.sitepoint.com/loop-through-json-response-javascript/
            searchedBooks.forEach(book => {
                console.log(book)
                // source: https://www.digitalocean.com/community/tutorials/how-to-add-javascript-to-html
                // https://www.geeksforgeeks.org/how-to-append-html-code-to-a-div-using-javascript/
                searchResultsDiv.innerHTML = `<h2>Search Results:</h2><h3>${book.book_title}</h3><p>${book.author_name}</p><p><img class="poster" src='${book.book_image}'/></p>`;

            });


        });
}

    document.querySelector('#title-form').addEventListener('submit', showBook);


    function addFavorite(evt){
        // To Do : add "not implemented" alert
        console.log("Test")
        alert("Favorite saved");
        // source: https://stackoverflow.com/questions/7822407/why-is-my-alert-showing-more-than-once
        const delFavButton = evt.target;
        const favorite_id = delFavButton.dataset.bookId;
        // const favoriteID = document.getElementById('favorite-button')
        // console.log("Test")
        fetch(`/favorites?${favorite_id}`)
        .then((response) => response.json())
        .then((favoritedBooks) => {
            // console.log(favoritedBooks)
            // source: https://www.sitepoint.com/loop-through-json-response-javascript/
            favoritedBooks.forEach(favoritedBook => {
                console.log(favoritedBook)
                // source: https://www.digitalocean.com/community/tutorials/how-to-add-javascript-to-html
                // https://www.geeksforgeeks.org/how-to-append-html-code-to-a-div-using-javascript/
                favoriteResultsDiv.innerHTML = `<h2>Favorites</h2><h3>${favoritedBook.book_title}</h3><p>${favoritedBook.author_name}</p><p><img class="poster" src='${favoritedBook.book_image}'/></p>`;

            });


        });
    }

    // fetch(`/books.json?favorite=${favorite_id}`)
    function removeFavorite(evt){
        // To Do : add "not implemented" alert
        alert("Favorite removed");
        // source: https://stackoverflow.com/questions/7822407/why-is-my-alert-showing-more-than-once
        evt.stopImmediatePropagation();
        // console.log("Test")
        const favButton = evt.target;
        const favorite_id = favButton.dataset.bookId;
        fetch(`/favorites?${favorite_id}`)
        .then((response) => response.json())
        .then((favoritedBooks) => {
            // console.log(favoritedBooks)
            // source: https://www.sitepoint.com/loop-through-json-response-javascript/
            favoritedBooks.forEach(favoritedBook => {
                console.log(favoritedBook)
                // source: https://www.digitalocean.com/community/tutorials/how-to-add-javascript-to-html
                // https://www.geeksforgeeks.org/how-to-append-html-code-to-a-div-using-javascript/
                favoriteResultsDiv.innerHTML = `<h2>Favorites</h2><h3>${favoritedBook.book_title}</h3><p>${favoritedBook.author_name}</p><p><img class="poster" src='${favoritedBook.book_image}'/></p>`;

            });


        });
    }
    // source: https://developer.mozilla.org/en-US/docs/Web/API/Document/DOMContentLoaded_event
    document.addEventListener('DOMContentLoaded', () => {
        // source: https://stackoverflow.com/questions/12330086/how-to-loop-through-selected-elements-with-document-queryselectorall
        document.querySelectorAll('.favorite-button').forEach(button =>{
        button.addEventListener('click', addFavorite);

    });

        document.querySelectorAll('.remove-favorite-button').forEach(button =>{
        button.addEventListener('click', removeFavorite);

    });

});


    // // source: https://www.basedash.com/blog/how-to-create-a-toggle-button-in-javascript

    // document.addEventListener('DOMContentLoaded', function() {
    //     var toggleButton = document.getElementById('favorite-button');
    //         toggleButton.addEventListener('click', function() {
    //           this.classList.toggle('active');
    //           // Additional state change actions can be performed here
    //           let isToggled = false;

    //           toggleButton.addEventListener('click', function() {
    //             isToggled = !isToggled;
    //             this.classList.toggle('active');
    //             // You may also want to trigger other actions based on the value of isToggled
    //           });
    //         });
    //     });