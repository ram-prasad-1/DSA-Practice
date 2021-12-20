`
def backtrack(path, seletionsList):
    for seletion in seletionsList:
        select
        backtrack(path, selectionList.slice(1))
        deselect
See: https://labuladong.gitbook.io/algo-en/iii.-algorithmic-thinking/detailsaboutbacktracking
`;

function related() {
  const p = require('../basics/pnc-permutation.js');
}

function getPermutations(arr) {
  const result = [];
  _addPermutations([], arr, result);

  return result;
}

function _addPermutations(path = [], selectionList = [], result = []) {
  console.log(path, selectionList);
  if (selectionList.length === 0) {
    result.push([...path]);
  }

  // for permutation, select means: fix this and permute the rest
  for (const [selectIndex, selection] of selectionList.entries()) {
    path.push(selection);
    _addPermutations(
      path,
      selectionList.filter((_, i) => i !== selectIndex),
      result
    );
    path.pop();
  }
}

const data = [...Array(3)].map((_, i) => i + 1);
const p = getPermutations(data);
console.log(p);
