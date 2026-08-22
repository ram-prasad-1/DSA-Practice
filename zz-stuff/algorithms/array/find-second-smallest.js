function fn(arr) {
  if (arr.length === 0) return null;
  if (arr.length === 1) return arr[0];

  let min = arr[0];
  let secMin = arr[1];

  if (secMin < min) {
    [min, secMin] = [secMin, min];
  }

  for (let i = 2; i < arr.length; i++) {
    if (arr[i] < secMin) {
      secMin = arr[i];
    }

    if (arr[i] < min) {
      secMin = min;
      min = arr[i];
    }
  }
  return secMin;
}

console.log(fn([5, -55, 3, 2, 10, 61]));
