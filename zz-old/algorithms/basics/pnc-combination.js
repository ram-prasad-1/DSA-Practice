const getCombinations = (arr) => {
  const result = [];
  const _traverse = (path, selectionList) => {
    result.push([...path]);

    for (const [selectIndex, selection] of selectionList.entries()) {
      path.push(selection);
      _traverse(path, [...selectionList].slice(selectIndex + 1));
      path.pop();
    }
  };

  _traverse([], arr);
  return result;
};

const data = [3, 5, 1];
const res = getCombinations(data);
console.log(res);
