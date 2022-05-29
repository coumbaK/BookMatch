
const displaysearch = () => {
    const html = 
    `<input type="text" name="search" placeholder="Search for a book">
    <button onclick = "displayresults(event);"> Search </button>`;

    document.querySelector('#search-bar').innerHTML = html;
};
const result2html = result => {
    return `
    <div class = "book-card">
    <img src="https://covers.openlibrary.org/b/ID/${result['ID']}-L.jpg">
    <div class = "title" >${result['Title']}</div>
    <div class = "author">${result['Author']}</div>
    <button class = "add-button">Add to Library</button>
</div>`
}

const displayresults = ev => {

    const elem = ev.currentTarget;
    const search = elem.parentElement.querySelector('input').value;

    
    fetch('/api/results?search= ' + search)

    
        .then(response => response.json())
        .then (results => {
            console.log(results);
            
            const html = results.slice(0,10).map(result2html).join('');
            document.querySelector('#search-results').innerHTML = html;
        })
        
    
};

        
displaysearch();