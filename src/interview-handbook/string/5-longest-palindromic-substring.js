`
Expand Around Center Approach: O(n^2)
`;
const longestPalindrome = function (str) {
  if (str.length <= 1) return str;
  let maxL = 0;
  let maxR = 0;

  for (let i = 1; i < str.length - 1; i = i + 1 / 2) {
    let pL = -1;
    let pR = -1;

    let left = Math.floor(i);
    let right = Math.ceil(i);
    while (left >= 0 && right <= str.length - 1) {
      if (str[left] !== str[right]) {
        break;
      }
      pL = left;
      pR = right;

      left -= 1;
      right += 1;
    }

    if (pR - pL > maxR - maxL) {
      maxR = pR;
      maxL = pL;
    }
  }

  return str.slice(maxL, maxR + 1);
};

console.log(longestPalindrome('atoantabccccbantaotano'));
