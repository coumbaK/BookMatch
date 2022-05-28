


const displayresults = () => {

    var search = document.querySelector('input').value;
    console.log(search);
    fetch('/api/results?text=${search}')

    
        .then(response => response.json())
        .then(data => {
            const 
            document.querySelector('#results').innerHTML = 

        

        


        

}

        



        
