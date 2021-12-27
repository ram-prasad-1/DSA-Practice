`
find the subset of an array of whole numbers with sum equal to a given target when array element can repeat themselves
https://www.youtube.com/watch?v=jgps7MXtKRQ
`;

function isScorePossible(arr, targetScore) {
  const sumPossibleArr = Array(targetScore + 1).fill(false);
  sumPossibleArr[0] = true; // by default zero score

  // i -> a score
  for (let i = 1; i < sumPossibleArr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      if (arr[j] <= i) {
        sumPossibleArr[i] = sumPossibleArr[i] || sumPossibleArr[i - arr[j]];
      }
      if (sumPossibleArr[i]) {
        break;
      }
    }
    sumPossibleArr[i] = sumPossibleArr[i] || false;
  }

  return sumPossibleArr[sumPossibleArr.length - 1];
}

console.log(isScorePossible([6, 3, 4, 5], 1));
