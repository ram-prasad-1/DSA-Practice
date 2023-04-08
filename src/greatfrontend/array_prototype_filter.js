// https://www.greatfrontend.com/questions/javascript/array-filter
Array.prototype.myCustomFilter = function (fn) {
  const filtered = []; // it will receive all values that match to condition passed in fn callback.

  for (let i = 0; i < this.length; i++) {
    if (fn(this[i])) {
      filtered.push(this[i]);
    }
  }

  return filtered;
};
