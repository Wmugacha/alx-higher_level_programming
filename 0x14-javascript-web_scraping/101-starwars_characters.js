#!/usr/bin/node
// script that prints all characters of a Star Wars movie in the same order as the JSON response.

const request = require('request');

const movieId = process.argv[2];

async function printCharacters (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  const response = await new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) console.error(error);
      else resolve(response);
    });
  });

  const data = JSON.parse(response.body);
  const characterUrls = data.characters;

  // Fetch characters data in the order they appear in the response
  const characters = await Promise.all(characterUrls.map(url =>
    new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) reject(error);
        else resolve(JSON.parse(body));
      });
    })
  ));

  // Print the names of the characters on separate lines in the order they appear in the response.

  characters.forEach(character => console.log(character.name));
}
printCharacters(movieId);
