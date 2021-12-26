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

const mm = [];

// fn(arr, 3, sum) === fn(arr, 5, sum)
function _canPartition(arr, i, sum, memo = mm) {
  if (i < 0) return false;
  if (sum === arr[i]) return true;
  if (sum - arr[i] < 0) return false;

  console.log(i, sum, ' --> ', i - 1, sum - arr[i], ' and ', i - 1, sum);
  const withInclusion = _canPartition(arr, i - 1, sum - arr[i], memo);
  const withExclusion = _canPartition(arr, i - 1, sum, memo);
  return withInclusion || withExclusion;
}

console.log(canPartition([2, 8, 6, 4, 14]));
console.log(mm);
