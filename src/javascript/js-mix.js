// JS is copy by reference value
let user = { name: 'virat' };
const list = [user];
user = null;

console.log(list); // prints [{name: 'virat'}]

// A nested function's this is not tied to the parent this. Consider it separately
const obj = {
  answer: 42,
  log() {
    console.log(this.answer);
    function inner() {
      console.log(this.answer);
    }
    inner();
  },
};

obj.log();

// Hoisting
var x = 23;
(function () {
  var x = 43;
  (function random() {
    x++;
    console.log(x);
    var x = 21;
  })();
})();
