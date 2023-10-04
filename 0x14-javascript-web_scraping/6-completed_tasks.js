#!/usr/bin/node

const request = require('request')

request(process.argv[2], function (err, resp, body) {
  if (err) {
    console.error(err);
  } else {
    const complete = {};
    body = JSON.parse(body);
    for (i = 0; i < body.length; i++) {
      const userId = body[i].userId;
      const cm = body[i].completed;
      if (cm && completed[userID]) {
        completed[userId] = 0;
      }

      if (cm) ++ completed[userId];
