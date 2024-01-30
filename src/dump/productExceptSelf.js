`
https://stackoverflow.com/a/68571008
`;

function productExceptSelf(nums) {
  const res = [];
  for (let i = 0; i < nums.length; i++) {
    if (i === 0) {
      res[i] = 1;
    } else {
      // = left product except i
      res[i] = res[i - 1] * nums[i - 1];
    }
  }

  let right = 1; // i+1 to last
  for (let i = nums.length - 1; i >= 0; i--) {
    res[i] = res[i] * right;
    right *= nums[i + 1];
  }

  return res;
}

n = [1, 2, 3, 4];
console.log(productExceptSelf(n));
