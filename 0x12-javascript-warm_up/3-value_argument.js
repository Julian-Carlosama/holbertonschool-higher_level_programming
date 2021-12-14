#!/usr/bin/node
const args = process.argv[2];
if (args) {
  console.log(args);
  process.exit(-1);
} else {
  console.log('No argument');
  process.exit(-1);
}
