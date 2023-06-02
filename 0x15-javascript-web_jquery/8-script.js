// Display list of Film titles from an API
$(document).ready(()=>{
$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', (data)=>{
  const titles = data.results.map((film) => film.title);

  titles.forEach((title) => {
    const titlesList = $('<li>').text(title);
    $('#list_movies').append(titlesList);
    });
  });
});
