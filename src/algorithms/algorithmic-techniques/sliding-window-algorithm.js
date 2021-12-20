`
https://labuladong.gitbook.io/algo-en/iii.-algorithmic-thinking/slidingwindowtechnique
`;

function findAllAnagrams(s, p) {
  const sArr = Array.from(s);
  const pArr = Array.from(p);
  pArr.sort();
  const pSorted = pArr.join('');

  let left = 0;
  let right = pArr.length - 1;
  const results = [];

  while (right < sArr.length) {
    const currentSlice = sArr.slice(left, right + 1);
    if (pSorted === currentSlice.sort().join('')) {
      results.push(left);
    }

    left += 1;
    right += 1;
  }

  return results;
}

console.log(findAllAnagrams('tntnqwftntnfwqtnat', 'qwf'));
