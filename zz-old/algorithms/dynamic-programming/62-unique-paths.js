`
https://www.youtube.com/watch?v=zQ6lx5tZ1Xw
`;

function findUniquePaths(m, n) {
  // dp[i][j] = Unique paths till dp[i][j]
  const dp = Array(m)
    .fill(null)
    .map(() => Array(n).fill(null));

  for (let i = 0; i < m; i++) {
    dp[i][0] = 1;
  }

  for (let i = 0; i < n; i++) {
    dp[0][i] = 1;
  }

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
    }
  }

  return dp[m - 1][n - 1];
}

console.log(findUniquePaths(3, 7));
