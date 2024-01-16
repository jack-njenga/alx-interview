#!/usr/bin/node
// requests for all character of Star Wars movie.

const request = require('request');
const filmId = process.argv[2];

request('https://swapi-api.alx-tools.com/api/films/' + filmId, function (error, response, body) {
  if (error) {
    console.error('error', error);
  }
  const result = JSON.parse(response.body);
  const characters = result.characters;
  let url;
  const names = {};
  let out = 0;

  for (let j = 0; j < characters.length; j++) {
    url = characters[j];
    request(url, function (error, response, body) {
      if (error) {
        console.error('error', error);
      }
      const data = JSON.parse(response.body);
      names[j] = data.name;
      out += 1;
      if (out === characters.length) {
        for (let i = 0; i < characters.length; i++) {
          console.log(names[i]);
        }
      }
    });
  }
});