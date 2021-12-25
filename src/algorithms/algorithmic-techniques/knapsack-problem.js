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
    const include = values[start] + _getMaxValue(start + 1, capacityLeft - weights[start]);
    const exclude = _getMaxValue(start + 1, capacityLeft);

    return Math.max(include, exclude);
  };

  return _getMaxValue(0, weightCapacity);
}

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

const weights = [4, 2, 1, 10, 2];
const values = [12, 2, 1, 4, 1];
const capacity = 15;

console.log(getMaxValue2(weights, values, capacity));
