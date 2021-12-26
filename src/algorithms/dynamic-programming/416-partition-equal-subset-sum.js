function canPartition(arr) {
  const sum = arr.reduce((agg, curr) => agg + curr, 0);
  const halfSum = sum / 2;
  if (sum % 2 === 1) return false;

  // just check if halfSum is possible or not
  return _canPartition(arr, 0, halfSum);
}

function _canPartition(arr, i, sum) {
  if (i >= arr.length - 1) return false;
  if (sum === arr[i]) return true;

  const withInclusion = _canPartition(arr, i + 1, sum - arr[i]);
  const withExclusion = _canPartition(arr, i + 1, sum);
  return withInclusion || withExclusion;
}

// backtracking
function canPartition2(arr) {
  const sum = arr.reduce((agg, curr) => agg + curr, 0);
  const halfSum = sum / 2;
  if (sum % 2 === 1) return false;

  const fn = (path, selectionList) => {
    const currSum = path.reduce((agg, curr) => agg + curr, 0);
    if (currSum === halfSum) return true;
    if (currSum > halfSum) return false;

    for (const [index, selection] of selectionList.entries()) {
      path.push(selection);
      const result = fn(path, selectionList.slice(index + 1));
      if (result === true) {
        return true;
      }
      path.pop();
    }
    return false;
  };
  return fn([], arr);
}
