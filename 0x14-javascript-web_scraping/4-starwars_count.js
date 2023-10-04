#!/usr/bin/node

const request = require('request');
const starwarsuri = process.argv[2]

let n = 0;
let i, j;
request.get(starwarsuri, function (err, res, body) {
  body = JSON.parse(body).results;
  for (i = 0; i < body.length; i++) {
    const ch = body[i].characters;
    for (j = 0; j < ch.length; j++) {
      const character = ch[j];
      const characterid = character.split('/')[5];
      if (characterid === '18') {
        n += 1;
      }
    }
  }
  console.log(n);
});
