#!/usr/bin/node

const request = require('request');
const fs = require('fs')
const url = process.argv[2];
const filepath = process.argv[3]




request.get(url, function (err, resp, body) {
  fs.writeFile(filepath, body, 'utf-8', function (err) {
    if (err) {
      console.error(err);
    }
  });
});
