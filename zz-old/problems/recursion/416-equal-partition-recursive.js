`
https://www.geeksforgeeks.org/partition-problem-dp-18/
`;

function canPartition(arr) {
  const sum = arr.reduce((agg, curr) => agg + curr, 0);
  const halfSum = sum / 2;
  if (sum % 2 === 1) return false;

  // just check if halfSum is possible or not
  return _canPartition(arr, arr.length - 1, halfSum);
}

function _canPartition(arr, i, sum) {
  if (i < 0) return false;
  if (sum === arr[i]) return true;
  if (sum - arr[i] < 0) return false;

  console.log(i, sum, ' --> ', i - 1, sum - arr[i], ' and ', i - 1, sum);
  const withInclusion = _canPartition(arr, i - 1, sum - arr[i]);
  const withExclusion = _canPartition(arr, i - 1, sum);
  return withInclusion || withExclusion;
}

console.log(canPartition([2, 8, 6, 4, 14]));
