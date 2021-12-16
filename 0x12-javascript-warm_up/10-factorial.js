#!/usr/bin/node
const convert = parseInt(process.argv[2]);
function factorialRecursivo (n) {
  if (!n) {
    return (1);
  }
  return (n * factorialRecursivo(n - 1));
}
console.log(factorialRecursivo(convert));
