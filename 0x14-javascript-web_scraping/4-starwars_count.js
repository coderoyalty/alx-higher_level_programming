#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const url = argv[2];
const charId = '18';

function handler (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode !== 200) {
    return;
  }
  const data = JSON.parse(body);
  const results = data.results;
  let total = 0;
  const resultHandler = (result) => {
    const characters = result.characters;
    characters.forEach((character) => {
      const tokens = character.split('/');
      const index = tokens.length - 2;
      if (tokens[index] === charId) {
        total++;
      }
    });
  };
  results.forEach(resultHandler);
  console.log(total);
}

request.get(`${url}`, handler);
