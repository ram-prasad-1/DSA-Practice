`
Curry
Currying: fn(a, b, c) = curriedFn(a)(b)(c)
https://www.greatfrontend.com/questions/javascript/curry

Qn. sum(4)(3)(7)('.') // returns 14
`;

// Trick: always return the nested function.
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
