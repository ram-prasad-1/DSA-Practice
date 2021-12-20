function related() {}

function getCombinations(arr, r) {
  const result = [];
  addCombinations([], arr, r, result);
  return result;
}

function addCombinations(path, selectionList, r, result) {
  if (path.length === r) {
    result.push([...path]);
    return;
  }

  for (const [index, selection] of selectionList.entries()) {
    path.push(selection);
    addCombinations(path, selectionList.slice(index + 1), r, result);
    path.pop();
  }
}

const data = [...Array(3)].map((_, i) => i + 1);

console.log(getCombinations(data, 2));
