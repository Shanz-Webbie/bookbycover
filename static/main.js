
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
    fetch(`/books.json?${book_title}`)
        .then((response) => response.json())
        .then((searchedBooks) => {
            console.log(searchedBooks)
            const searchResultsDiv = document.querySelector('#search-results');
            searchedBooks.forEach(book => {
                console.log(book)
                searchResultsDiv.innerHTML = `<h3>${book.book_title}</h3><p>${book.author_name}</p><p><img class="poster" src='${book.book_image}'</p>`;
            });

            // document.querySelector('#search-results').innerHTML= searchedBooks});


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

                // // let placeholder = document.querySelector('#search-results');
            // let out = "";
            // for (let book of searchedBooks){
            //     out += `
            //     <p><img src='${book.book_image}'</p><br>

            //     `;
            // }
            // for(const title of title.books ) {
            //     const listBook = document.createElement("strong").textContent =
            //     title.book_title;
            //     listItem.append(` Here are your search results ${title.book_title}`);
            //     // listItem.appendChild(document.createElement("strong")).textContent =
            //     //   `£${product.Price}`;
            //     // myList.appendChild(listItem);
            //   }
            // })
            // let jsonobj=JSON.parse()
            // console.log(jsonobj)
            // document.querySelector('#search-results')
            // document.getElementById("title").innerHTML = `Title: ${response.book_title}`});
            // document.querySelector('#search-results').innerHTML= JSON.stringify(title)});