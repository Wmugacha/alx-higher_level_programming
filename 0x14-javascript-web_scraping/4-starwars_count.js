#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present
// Usage: ./4-starwars_count.js https://swapi-api.alx-tools.com/api/films

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.error(error);

  const data = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < data.results.length; i++) {
    const character = data.results[i].characters;
    for (let k = 0; k < character.length; k++) {
      if (character[k].includes('18')) {
        count = count + 1;
      }
    }
  }
  console.log(count);
});
