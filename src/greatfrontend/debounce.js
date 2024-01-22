// trick: just call the fn after the delay and keep delaying if called prematurely
// Note: don't wait for another fn call after wait is over.

function debounce(func, wait = 0) {
  let timeoutID = null;
  return function (...args) {
    clearTimeout(timeoutID);

    // Trick: `this` keyword should be linked to the function used by the outer world.
    // Other local/nested functions can ignore `this` considerations by using arrow functions.
    timeoutID = setTimeout(() => {
      func.apply(this, args);
    }, wait);
  };
}
