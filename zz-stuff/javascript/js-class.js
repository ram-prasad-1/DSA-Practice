// Trick: All methods inside the class are added to the prototype property of the class object.
class User {
  constructor(name) {
    this.name = name;
  }

  sayHello() {
    console.log(`hi ${this.name}`);
  }
}

// is same as
function User(name) {
  this.name = name;
}

// // All function prototypes already have a property called constructor so it is not added here.
User.prototype.sayHello = function () {
  console.log(`hi ${this.name}`);
};
