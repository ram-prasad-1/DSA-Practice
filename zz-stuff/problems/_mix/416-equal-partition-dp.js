`
https://www.geeksforgeeks.org/partition-problem-dp-18/
`;

function canPartition(arr) {
  const sum = arr.reduce((agg, curr) => agg + curr, 0);
  const halfSum = sum / 2;
  if (sum % 2 === 1) return false;

  // just check if halfSum is possible or not
  return _isSumPossible(arr, halfSum);
}

function _isSumPossible(arr, sum) {
  const sumArr = Array(sum + 1).fill(false);
  sumArr[0] = true;

  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < sumArr.length; j++) {
      if (j >= arr[i]) {
        sumArr[j] = sumArr[j - arr[i]] || sumArr[j];
      }
    }
  }
  return sumArr[sum];
}

console.log(canPartition([2, 8, 6, 4, 14]));
