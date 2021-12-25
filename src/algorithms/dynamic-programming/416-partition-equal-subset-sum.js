// backtracking
function canPartition(arr) {
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

console.log(canPartition([1, 5, 11, 5, 4, 12, 8]));
