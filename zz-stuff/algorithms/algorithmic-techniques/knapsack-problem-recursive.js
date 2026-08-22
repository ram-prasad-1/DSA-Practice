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

// Qn. Get max. value of the weighted items if capacity is given.
const weights = [4, 2, 1, 10, 2];
const values = [12, 2, 1, 4, 1];
const capacity = 15;

console.log(getMaxValue(weights, values, capacity));
