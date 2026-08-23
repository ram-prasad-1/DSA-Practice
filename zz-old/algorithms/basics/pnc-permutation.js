// https://labuladong.gitbook.io/algo-en/iii.-algorithmic-thinking/subset_permutation_combination
// https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

const getPermutations = (arr) => {
  const result = [];
  const _traverse = (path, selectionList) => {
    if (selectionList.length === 0) {
      result.push([...path]);
    }

    for (const [selectIndex, selection] of selectionList.entries()) {
      path.push(selection);
      _traverse(
        path,
        selectionList.filter((_, i) => i !== selectIndex)
      );
      path.pop();
    }
  };

  _traverse([], arr);
  return result;
};

const data = [3, 5, 1];
getPermutations(data);
