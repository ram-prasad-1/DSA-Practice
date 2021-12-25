`
https://learnersbucket.com/examples/algorithms/knapsack-problem-in-javascript/
`;
function getMaxValue(weights, values, weightCapacity) {
  const _getMaxValue = (start, capacityLeft) => {
    // base case: reject if capacity < 0
    if (capacityLeft < 0) {
      return Number.MIN_SAFE_INTEGER;
    }

    // base case: no value change if either capacity or weights are exhausted
    if (start > values.length - 1 || capacityLeft === 0) {
      return 0;
    }
    let include = values[start] + _getMaxValue(start + 1, capacityLeft - weights[start]);
    let exclude = _getMaxValue(start + 1, capacityLeft);

    return Math.max(include, exclude);
  };

  return _getMaxValue(0, weightCapacity);
}

const weights = [4, 2, 1, 10, 2];
const values = [12, 2, 1, 4, 1];
const capacity = 15;

console.log(getMaxValue(weights, values, capacity));
