#!/usr/bin/node
if (process.argv.length <= 2) {
  console.log('No argument');
  process.exit(-1);
} else if (process.argv.length === 3) {
  console.log('Argument found');
  process.exit(-1);
} else {
  console.log('Arguments found');
  process.exit(-1);
}
