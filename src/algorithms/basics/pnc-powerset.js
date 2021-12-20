// https://github.com/trekhleb/javascript-algorithms/tree/master/src/algorithms/sets/power-set
// https://en.wikipedia.org/wiki/Power_set
// C(n, 0) + C(n, 1) + … + C(n, n) = 2^n --> n(all subsets of a set)

function getPowerSet(arr) {
  const result = [];
  _makePowerSet([], arr, result);
  return result;
}

function _makePowerSet(path = [], selectionList, result) {
  for (const selection of selectionList) {
    path.push(selection);

    _makePowerSet(path, selectionList.slice(1));
    path.pop();
  }
}

const swap = (arr, a, b) => ([arr[b], arr[a]] = [arr[a], arr[b]]);

const arr = [34, 64, 75];
