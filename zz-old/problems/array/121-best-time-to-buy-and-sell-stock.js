`
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
`;
function maxProfit(prices) {
  return _maxProfit([], prices, 0);
}

function _maxProfit(path, selectionList, max) {
  if (path.length === 2) {
    return Math.max(max, path[1] - path[0]);
  }

  for (const [index, selection] of selectionList.entries()) {
    path.push(selection);
    max = _maxProfit(path, selectionList.slice(index + 1), max);
    path.pop();
  }

  return max;
}

`
approach 2: Find the largest peak following the smallest valley.
`;

console.log(maxProfit([4, 12, 2, 20, 32]));
