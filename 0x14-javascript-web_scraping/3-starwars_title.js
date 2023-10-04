#!/usr/bin/node

const request = require('request');
const starwarsuri = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);


request.get(starwarsuri, function (err, res, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
