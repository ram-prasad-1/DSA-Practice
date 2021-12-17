let x = {};

// type
let y = typeof x === 'object'; // object, function, boolean, string, number
// typeof null === 'object'; => true
Array.isArray(x);
console.log(x === undefined);

// control structures
if (x === 99) {
}

while (true) {
  y = 11;
  if (x !== 100) {
    break;
  }
}

switch (x) {
  case 'tnato':
    console.log('111');
    break;
  default:
    console.log('last');
}
