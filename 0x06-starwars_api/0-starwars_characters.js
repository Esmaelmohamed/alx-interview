#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Star Wars API films endpoint for the specific movie
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (err, res, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  // Loop through each character URL and get their name
  characters.forEach((characterUrl) => {
    request(characterUrl, (charErr, charRes, charBody) => {
      if (charErr) {
        console.error('Error:', charErr);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});

