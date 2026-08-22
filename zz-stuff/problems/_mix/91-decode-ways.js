`
https://www.pepcoding.com/resources/online-java-foundation/dynamic-programming-and-greedy/count_encodings/topic
`;

function numDecodings(s) {
  if (s.length === 1) return +s > 0;

  let ways = 1;
  let i = 1;
  while (i < s.length) {
    const ss = s.slice(i - 1, i + 1);
    if (ss[0] === '0' || ss[1] === '0') {
      continue;
    }

    if (+ss >= 11 && +ss <= 26) {
      ways += 1;
    }
    i++;
  }

  return ways;
}

console.log(numDecodings('121'));
