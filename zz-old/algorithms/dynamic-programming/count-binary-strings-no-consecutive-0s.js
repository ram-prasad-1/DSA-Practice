`
https://www.pepcoding.com/resources/online-java-foundation/dynamic-programming-and-greedy/count_binary_strings/topic
dp0[i] = dp1[i-1]
dp1[i]I = dp0[i-1] +dp1[i-1]

dp0 --> count of binary strings of length i + 1, ending with 0.
`;

function countBs(n) {
  let s0 = 1;
  let s1 = 1;

  for (let i = 2; i <= n; i++) {
    const tmp = s0;
    s0 = s1;
    s1 = tmp + s1;
  }

  return s0 + s1;
}

console.log(countBs(2));
