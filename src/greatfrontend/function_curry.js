`
Implement curry function which should work like this
function multiply(a, b, c) {  return a * b * c;}
let curried = curry(multiply);
console.log(curried(2)(3)(4)); // 24
console.log(curried(2, 3)(4));  // 24
console.log(curried(2, 3, 4));  // 24
console.log(curried(5)(6, 7)); // 210
`;

function curry(fn) {
  return function _curry(...args) {
    if (args.length >= fn.length) {
      return fn.apply(this, args);
    } else {
      return function (...args2) {
        return _curry.apply(this, args.concat(args2));
      };
    }
  };
}

function multiply(a, b, c) {
  return a * b * c;
}
let curried = curry(multiply);
console.log(curried(2)(3)(4)); // 24
console.log(curried(2, 3)(4)); // 24
