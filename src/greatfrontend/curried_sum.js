`
Curry
Currying: fn(a, b, c) = curriedFn(a)(b)(c)
https://www.greatfrontend.com/questions/javascript/curry

Qn. sum(4)(3)(7)('.') // returns 14
`;

// Trick: Use inner function for everything including for returning.
// Trick: A function can call itself (from it's body), that's how recursion algos work.
// myFn.length = no of function params
function sum(a) {
  let total = a;
  const _sumInner = (b) => {
    if (b === '.') {
      return total;
    }
    total += b;
    return _sumInner;
  };

  return _sumInner;
}

console.log(sum(4)(3)(7)('.'));
