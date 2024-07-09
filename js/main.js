
const searchInput = document.getElementById('bookSearch');
const searchButton = document.getElementById('searchButton');

searchButton.addEventListener('click', function(){
    const searchQuery = searchInput.value;
    console.log(`Searching for '${searchQuery}'...`);

});