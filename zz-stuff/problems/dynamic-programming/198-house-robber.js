function rob(nums) {
  let prevInc = 0;
  let prevEx = 0;
  let max = 0;

  for (let i = 0; i < nums.length; i++) {
    const currentInc = prevEx + nums[i];
    const currentEx = prevInc;
    max = Math.max(currentInc, currentEx);

    prevInc = currentInc;
    prevEx = currentEx;
  }

  return max;
}

console.log(rob([2, 7, 9, 3, 1]));
