`
find the subset of an array of whole numbers with sum equal to a given target when array element can repeat themselves
https://www.youtube.com/watch?v=jgps7MXtKRQ
`;

function isScorePossible(arr, targetScore) {
  const scores = Array(targetScore + 1).fill(false);
  scores[0] = true; // by default zero score

  // Trick: keep on building optimal substructures starting with smallest set
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < scores.length; j++) {
      const val = arr[i];
      if (j >= val) {
        // checks both the cases: 1. item included and item 2. item excluded
        scores[j] = scores[j - val] || scores[j];
      }
    }
  }

  return scores[scores.length - 1];
}

console.log(isScorePossible([6, 3, 2, 4], 7));
