#!/usr/bin/node
// Script that prints all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) console.error(error);

  const data = JSON.parse(body);

  const characters = [];

  for (let i = 0; i < data.characters.length; i++) {
    request(data.characters[i], (error, response, body) => {
      if (error) console.error(error);

      const character = JSON.parse(body);

      characters.push(character.name);

      if (characters.length === data.characters.length) {
        console.log(characters.join('\n'));
      }
    });
  }
});
