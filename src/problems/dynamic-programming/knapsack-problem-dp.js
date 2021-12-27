`
https://learnersbucket.com/examples/algorithms/knapsack-problem-in-javascript/
`;

function getMaxValue(weights, values, weightCapacity) {
  const table = Array(weights.length + 1)
    .fill(null)
    .map(() => Array(weightCapacity + 1).fill(null));

  for (let i = 0; i < table.length; i++) {
    for (let j = 0; j < table[0].length; j++) {
      if (i === 0 && j === 0) {
        // empty set, 0 score
        table[i][j] = 0;
      } else if (i === 0) {
        // empty set
        table[i][j] = 0;
      } else if (j === 0) {
        // 0 score
        table[i][j] = 0;
      } else {
        // Qn: To include it or not?
        // Only include if we have enough capacity left and outcome becomes desirable
        // otherwise just carry forward.
        const currWt = weights[i - 1];
        const valueWithInclusion = values[i - 1] + table[i - 1][j - currWt];
        if (j >= currWt && valueWithInclusion >= table[i - 1][j]) {
          table[i][j] = valueWithInclusion;
        } else {
          table[i][j] = table[i - 1][j];
        }
      }
    }
  }
  console.log(table);
  return table[table.length - 1][table[0].length - 1];
}

const weights = [4, 2, 1, 10, 2];
const values = [12, 2, 1, 4, 1];
const capacity = 15;

console.log(getMaxValue(weights, values, capacity));
