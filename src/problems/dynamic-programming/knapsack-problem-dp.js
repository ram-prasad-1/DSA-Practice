`
https://youtu.be/-kedQt2UmnE?t=203
`;
function getMaxValue(weights, values, weightCapacity) {
  let maxValue = Number.MIN_SAFE_INTEGER;
  const _getMaxValue = (path, start) => {
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
      _getMaxValue(path, i + 1);
      path.pop();
    }
  };
  _getMaxValue([], 0);
  return maxValue;
}

const weights = [4, 2, 1, 10, 2];
const values = [12, 2, 1, 4, 1];
const capacity = 15;

console.log(getMaxValue(weights, values, capacity));
