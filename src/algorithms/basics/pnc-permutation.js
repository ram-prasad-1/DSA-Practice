// https://labuladong.gitbook.io/algo-en/iii.-algorithmic-thinking/subset_permutation_combination
// https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

function permutations(array = [], solution = [], start = 0) {
  if (start === array.length - 1) {
    solution.push([...array]);
  } else {
    // for the loop startIndex is fixed
    for (let index = start; index < array.length; index++) {
      // select
      swap(array, start, index);
      permutations(array, solution, start + 1);
      // deselect
      swap(array, start, index);
    }
  }

  return solution;
}

function swap(array, from, to) {
  [array[from], array[to]] = [array[to], array[from]];
}

const nums = [...Array(3)].map((_, i) => i + 1);
console.log(permutations(nums));
