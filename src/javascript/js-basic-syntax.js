let x = {};
let n = 8;
let thisArg = {};
let argArr = [n, x];
let arr = [n, x];
let target = {};
let source1 = {};
let source2 = {};
let sources = [];
`
basic iteration:
Turn other data types into an array and for array:
    - Use for..of
        * Use arr.entries() if required
    - Use for..i or while loop if infinite looping or index jumps needed
    - only in forEach() we can't break out from the loop.

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

// Object assign
Object.assign(target, source1, source2); // returns target object

// type
// Trick: There is no type known as null, array or NaN.
// Trick2: NAN has no self type
let y = typeof x === 'object'; // object, function, boolean, string, number
x = typeof null === 'object'; // true
x = typeof arr === 'object'; // true
// Trick: NaN: Not a number but at least type is number
x = typeof NaN === 'number'; // true
x = x === undefined;
Array.isArray(x);
// type coercion
x = 2 + '5'; // Equality // 25

`
 - SameValue: Object.is() [check literal value]
 - IsStrictlyEqual: ===  [check actual value but NaN are different]
     - IsLooselyEqual: == [type conversion + ===]
 - SameValueZero: no builtin [check actual value with NaN are same]

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness#strict_equality_using
`;
x = NaN !== NaN; // only case in which (x !== x) is true is when x is NaN
x = null == undefined; // true (falsey values are converted to boolean)

// control structures
if (x === 99) {
}

for (const [key, value] of Object.entries(obj)) {
  console.log(key, value);
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

// call, apply and bind
fn.bind(thisArg); // returns new function

// Trick: apply needs array
fn.apply(thisArg, argArr);
fn.call(thisArg, ...argArr);
Array.prototype.filter.call([4, null, 66], (value) => value);

// Prototypes
`
When it comes to inheritance, JavaScript only has one construct: objects.
Each object has a private property which holds a link to another object
called its prototype.
`;
x = obj.__proto__; // prototype object of obj
// function also have this additional property called prototype.
// it is used to set __proto__ when creating new objects using new Fn() syntax.
x = fn.prototype;

// Mix snippets
// generate array of n items
// Trick: Array(n) slots are totally empty. No memory assigned yet.
[...Array(n)].map(() => {});

// swap
const swap = (arr, a, b) => ([arr[b], arr[a]] = [arr[a], arr[b]]);
