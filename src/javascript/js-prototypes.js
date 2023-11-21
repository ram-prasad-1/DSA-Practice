`
obj.__proto__ ⇒ Prototype object of obj
Fn.prototype ⇒ (only for function objects) Used to set __proto__ for new Fn objects.

const obj = new Fn();
obj.__proto__ === Fn.prototype; // true


// Fn.prototype is just a regular property, by default = { constructor };
`;

const root = {
  answer: 42,
};

function LifeFn() {
  this.work = 'Teaching';
}

LifeFn.prototype = root;

const obj = new LifeFn();

console.log(obj.__proto__ === LifeFn.prototype);
