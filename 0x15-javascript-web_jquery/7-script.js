// Get character name from star wars API

$(document).ready(()=>{
$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data)=>{
  $('#character').text(data.name)
  });
});
