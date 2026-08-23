`

See: https://labuladong.gitbook.io/algo-en/iii.-algorithmic-thinking/detailsaboutbacktracking

def backtrack(path, seletionsList):
    for seletion in seletionsList:
        select
        backtrack(path, selectionList.slice(1))
        deselect
`;

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
