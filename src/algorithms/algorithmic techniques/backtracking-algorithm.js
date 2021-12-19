const permutationExample = require('../basics/pnc-permutation.js')`
P
def backtrack(...):
    for seletion in seletions List:
        select
        backtrack(...)
        deselect
See: https://labuladong.gitbook.io/algo-en/iii.-algorithmic-thinking/detailsaboutbacktracking
`;

const result = [];
function getPermutations(arr) {
  backtrack([], [...arr]);
}

function backtrack(path, selectionList) {
  for (const selection of selectionList) {
    path.push(selection);
  }
}

const nums = [...Array(10)].map((_, i) => i + 1);
console.log(getPermutations(nums));
