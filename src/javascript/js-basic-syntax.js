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
Trick: Only static methods you need to remember are converting to an array methods.

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

// Object
// object literal syntax
let obj = {
  // Property names are automatically coerced into a string. Value can be anything including functions
  // Quotes can be omitted if the property name is a numeric literal or a valid identifier
  name: 'John',
  logger() {},
  // computed property name
  [x]: 111,
};
obj.prop = 9;
obj['prop-2'] = 99;
obj[x] = 10; // computed property name

// type
let y = typeof x === 'object'; // object, function, boolean, string, number
// typeof null === 'object'; => true
// typeof NaN === 'number; => true
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

// Mix snippets

// generate array of n items
// Trick: Array(n) slots are totally empty. No memory assigned yet.
[...Array(n)].map(() => {});

// swap
const swap = (arr, a, b) => ([arr[b], arr[a]] = [arr[a], arr[b]]);
