`
find the subset of an array of whole numbers with sum equal to a given target
https://www.youtube.com/watch?v=tRpkluGqINc
`;

function isScorePossible(arr, targetScore) {
  // 2D array = An array of rows
  const table = Array(arr.length + 1)
    .fill(null)
    .map(() => Array(targetScore + 1).fill(-1));

  // i represents an index in the set of empty set + the given set
  // j represents a score
  for (let i = 0; i < table.length; i++) {
    for (let j = 0; j < table[0].length; j++) {
      if (i === 0 && j === 0) {
        // empty set, 0 score
        table[i][j] = true;
      } else if (i === 0) {
        // empty set
        table[i][j] = false;
      } else if (j === 0) {
        // 0 score
        table[i][j] = true;
      } else {
        const val = arr[i - 1];
        // Qn: To include it or not?
        // Only include if we have enough capacity left and outcome becomes desirable
        // otherwise just carry forward.
        if (j >= val && table[i - 1][j - val] === true) {
          table[i][j] = true;
        } else {
          table[i][j] = table[i - 1][j];
        }
      }
    }
  }

  console.log(table);
  return table[arr.length][targetScore];
}

console.log(isScorePossible([1, 3, 2], 5));
