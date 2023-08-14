#!/usr/bin/node

const myVar = process.argv;
const check = parseInt(myVar[2], 10);

if (!isNaN(check)) {
  console.log('My number: ' + check);
} else {
  console.log('Not a number');
}
