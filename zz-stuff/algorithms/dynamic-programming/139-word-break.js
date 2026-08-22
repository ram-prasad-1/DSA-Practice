`
https://www.youtube.com/watch?v=2NaaM_z_Jig
`;
function canBreak(s, wordDict) {
  wordDict = new Set(wordDict);

  const arr = Array(s.length + 1).fill(false);
  arr[0] = true;

  for (let i = 1; i < arr.length; i++) {
    let start = i - 1;
    const end = i - 1;
    while (start >= 0) {
      const c1 = wordDict.has(s.slice(start, end + 1));
      const c2 = arr[start] === true;
      if (c1 && c2) {
        arr[i] = true;
        break;
      }
      start -= 1;
    }
  }

  return arr[arr.length - 1];
}

console.log(canBreak('leetcode', ['leet', 'code']));

console.log(canBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']));

console.log(canBreak('catsanddog', ['cats', 'dog', 'sand', 'and', 'cat']));
