// https://www.greatfrontend.com/questions/javascript/array-filter
// Trick: it will be called as arr.myFn() so this object = arr here.
Array.prototype.myFn = function (fn) {
  const filtered = [];

  for (let i = 0; i < this.length; i++) {
    if (fn(this[i])) {
      filtered.push(this[i]);
    }
  }

  return filtered;
};
