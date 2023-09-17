const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
const hello = fetch(url)
    .then(response => response.json())
    .then(data => {
        document.getElementById('hello').innerHTML = data.hello;
    }
    );
