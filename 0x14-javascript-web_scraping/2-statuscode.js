#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function (err, resp) {
  console.log('code:', resp.statuscode);
});
