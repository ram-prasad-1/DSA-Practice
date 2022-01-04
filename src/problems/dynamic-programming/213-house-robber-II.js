function robCircular(nums) {
  const firstIncluded = _rob(nums.slice(0, nums.length - 1));

  const firstExcluded = _rob(nums.slice(1));

  return Math.max(firstIncluded, firstExcluded);
}

function _rob(nums) {
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

console.log(robCircular([1, 2, 3]));
