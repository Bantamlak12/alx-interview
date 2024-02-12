#!/usr/bin/node
// A script that prints all characters of a Star Wars movie
const request = require('request');

const starWarsCharacter = (id) => {
  request(
    `https://swapi-api.alx-tools.com/api/films/${id}/`,
    (err, res, body) => {
      if (err) {
        console.error('Error:', err);
      } else if (res.statusCode !== 200) {
        console.error('Status:', res.statusCode);
      } else {
        const films = JSON.parse(body);
        const filmCharacters = films.characters.map((url) => {
          return new Promise((resolve, reject) => {
            request(url, (err, res, body) => {
              if (err) reject(err);
              else {
                try {
                  const characters = JSON.parse(body);
                  resolve(characters.name);
                } catch {
                  reject(err);
                }
              }
            });
          });
        });

        Promise.all(filmCharacters).then((characters) => {
          characters.forEach((character) => {
            console.log(character);
          });
        });
      }
    }
  );
};

const id = parseInt(process.argv[2]);
if (isNaN(id)) console.log('Please use a number as an ID.');
else starWarsCharacter(id);
