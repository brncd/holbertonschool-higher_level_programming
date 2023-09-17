const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const movies = fetch(url)
    .then(response => response.json())
    .then(data => {
        const list = document.getElementById('list_movies');
        for (const movie of data.results) {
            const li = document.createElement('li');
            li.innerText = movie.title;
            list.appendChild(li);
        }
    }
    );
