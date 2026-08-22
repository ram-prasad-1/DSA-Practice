// no delay in throttle. and call immediately if the wait is over.
// Trick: wake up the function manually after the wait is over.

function throttle(func, wait = 0) {
  let isSleeping = false;

  return function (...args) {
    if (isSleeping) {
      return;
    }

    func.apply(this, args);
    isSleeping = true;

    setTimeout(function () {
      isSleeping = false;
    }, wait);
  };
}
