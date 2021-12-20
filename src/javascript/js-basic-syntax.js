let x = {};
let n = 8;

`
basic iteration:
Turn other data types into an array and for array:
    - Use for..of
        * Use arr.entries() if required
    - Use for..i or while loop if need to jump indexes while looping

For indefinite looping, use while loop


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

--------
Array

Remove items in-place: arr.splice()
Get new array with some items removed: arr.filter()
    - Create a slice: arr.slice()

Get a mapped array: arr.map()

From Array:
    - to String: arr.join()
    - to Set: new Set(arr)

`;

// generate array of n items
[...Array(n)].map(() => {});

// object
let obj = {
  name: 'John',
  logger() {},
};
obj.prop = 9;
obj['prop-2'] = 99;

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
