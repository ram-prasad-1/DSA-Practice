// no delay in throttle. and call immediately if the wait is over

function throttle(func, wait = 0) {
  let waitActive = false;

  return function (...args) {
    if (waitActive) {
      return;
    }

    func.apply(this, args);
    waitActive = true;

    setTimeout(function () {
      waitActive = false;
    }, wait);
  };
}
