`
https://leetcode.com/problems/two-sum/
`;

function twoSum(nums, target) {
  const memo = {};
  for (const [index, num] of nums.entries()) {
    // b = sum - a
    if (memo.hasOwnProperty(target - num)) {
      return [memo[target - num], index];
    } else {
      memo[num] = index;
    }
  }
}

console.log(twoSum([24, 53, 55, 12, 7], 65));
