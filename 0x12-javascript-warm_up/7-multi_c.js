#!/usr/bin/node

const myVar = process.argv;
const check = parseInt(myVar[2], 10);
let index = 0;

if (!isNaN(check)) {
  while (index < check) {
    console.log('C is fun');
    index++;
  }
} else {
  console.log('Missing number of occurrences');
}
