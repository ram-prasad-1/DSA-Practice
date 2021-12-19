let x = {};
let n = 8;

`
basic iteration:
Turn other data types into an array and for array:
    - Use arr.forEach() if no termination is required
    - Use for..of otherwise
        * Use arr.entries() if required

For other use cases, try while or for-i loop


To Array:
    - from 2d: Object.entries()
    - from 1d: Array.from(str/set)

--------
if has property/item:
1. 2D Object:
    obj.hasOwnProperty()

2. 1D items:
    String and array has same api
    - str.includes(), arr.includes(), set.has()
    - To get index: indexOf(), lastIndexOf()
`;

// generate array of n items
[...Array(n)].map(() => {});

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
