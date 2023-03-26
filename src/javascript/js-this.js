`
Tricks:
'this' points to an object. It is generally used inside an function.
The value of this is evaluated during the run-time, depending on the context.
And it is determined by how a function is called.

Only three rules: fn(), obj.fn(), new Fn().

Note:
- The bind() method can set the value of a function's this regardless of how it's called
- this value inside of an arrow function resolves to the one from the outer function.
  As it doesn't define it's own execution context.
- this is not inheritable. It will always be either global obj or obj to the left of the dot
  (or undefined in case of strict mode).
`;

const test = {
  prop: 42,
  func: function () {
    return this.prop;
  },
  arrowFunc: () => {
    return this.prop;
  },
};

console.log(test.func()); // 42
console.log(test.arrowFunc()); // undefined

function Test() {
  this.prop = 44;
}

console.log(new Test().prop); // 44
