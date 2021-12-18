// https://github.com/amejiarosario/dsa.js-data-structures-algorithms-javascript/blob/master/book/content/part02/array.asc#max-subarray
function maxSumArr(arr) {
  let overAllmax = arr[0];
  for (let i = 0; i <= arr.length - 1; i++) {
    let sum = 0;
    for (let j = i; j <= arr.length - 1; j++) {
      sum += arr[j];
      overAllmax = Math.max(overAllmax, sum);
    }
  }

  return overAllmax;
}

console.log(maxSumArr([-3, 4, -1, 2, 1, -5]));
