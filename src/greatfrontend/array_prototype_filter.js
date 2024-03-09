// https://www.greatfrontend.com/questions/javascript/array-filter
// Trick: it will be called as arr.myFn() so this object = arr here.
Array.prototype.myFn = function (fn) {
  const arr = this;

  const filtered = [];
  for (let i = 0; i < arr.length; i++) {
    if (fn(arr[i])) {
      filtered.push(arr[i]);
    }
  }

  return filtered;
};
