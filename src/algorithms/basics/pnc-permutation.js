// https://labuladong.gitbook.io/algo-en/iii.-algorithmic-thinking/subset_permutation_combination
// https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
function related() {
  const a = require('../algorithmic-techniques/backtracking-algorithm');
}

function addPermutations(array = [], start = 0, result = []) {
  if (start === array.length - 1) {
    result.push([...array]);
  } else {
    // for the loop startIndex is fixed
    for (let index = start; index < array.length; index++) {
      // select
      swap(array, start, index);
      addPermutations(array, start + 1, result);
      // deselect
      swap(array, start, index);
    }
  }
}

const swap = (arr, a, b) => ([arr[b], arr[a]] = [arr[a], arr[b]]);

const data = [...Array(3)].map((_, i) => i + 1);
const p = [];
addPermutations(data, 0, p);
console.log(p);
