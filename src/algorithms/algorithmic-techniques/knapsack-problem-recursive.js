`
https://learnersbucket.com/examples/algorithms/knapsack-problem-in-javascript/
`;
function getMaxValue(weights, values, weightCapacity) {
  const _getMaxValue = (end, capacityLeft) => {
    // base case: reject if capacity < 0
    if (capacityLeft < 0) {
      return Number.MIN_SAFE_INTEGER;
    }

    // base case: no value change if either capacity or weights are exhausted
    if (end < 0 || capacityLeft === 0) {
      return 0;
    }
    const include = values[end] + _getMaxValue(end - 1, capacityLeft - weights[end]);
    const exclude = _getMaxValue(end - 1, capacityLeft);

    return Math.max(include, exclude);
  };

  return _getMaxValue(weights.length - 1, weightCapacity);
}

const weights = [4, 2, 1, 10, 2];
const values = [12, 2, 1, 4, 1];
const capacity = 15;

console.log(getMaxValue(weights, values, capacity));

// Solution 2: backtracking
function getMaxValue2(weights, values, weightCapacity) {
  let maxValue = Number.MIN_SAFE_INTEGER;
  const _getMaxValue2 = (path, start) => {
    const wtSum = path.reduce((agg, current) => agg + weights[current], 0);
    if (wtSum <= weightCapacity) {
      maxValue = Math.max(
        maxValue,
        path.reduce((agg, current) => agg + values[current], 0)
      );
    } else {
      return;
    }
    for (let i = start; i < weights.length; i++) {
      path.push(i);
      _getMaxValue2(path, i + 1);
      path.pop();
    }
  };
  _getMaxValue2([], 0);
  return maxValue;
}
