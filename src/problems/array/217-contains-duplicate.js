function containsDuplicate(nums) {
  const memo = {};
  for (const num of nums) {
    if (memo.hasOwnProperty(num)) {
      memo[num] += 1;
    } else {
      memo[num] = 1;
    }
  }

  for (const [k, v] of memo.entries()) {
    if (v > 1) {
      return true;
    }
  }
  return false;
}
