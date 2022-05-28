

const displayresults = () => {
    fetch('/api/results')
        .then(response => response.json())
        .then(data => console.log(data))
        

}
        
        displayresults();

        
