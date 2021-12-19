`
F(n) is nth item in Fibonacci Sequence.
First 2 items are 1.
F(n) = F(n-1) + F(n-2)

Time complexity: O(2^n)
See: https://stackoverflow.com/a/45618079/3565194

Trick: consider start with binary numbers. 0, 1
`;

function getFibNum(n) {
  if (n === 1 || n === 2) return 1;
  return getFibNum(n - 1) + getFibNum(n - 2);
}

function getFibNumOptimized(n) {
  const memory = [1, 1];
  for (let i = 2; i <= n - 1; i++) {
    memory[i] = memory[i - 1] + memory[i - 2];
  }

  return memory[n - 1];
}

function getFibNumOptimizedTopDown(n) {
  if (n === 1 || n === 2) return 1;

  const cache = {};
  if (!cache[n]) {
    cache[n] = getFibNumOptimizedTopDown(n - 1) + getFibNumOptimizedTopDown(n - 2);
  }

  return cache[n];
}

console.log(getFibNumOptimizedTopDown(7) === getFibNum(7), getFibNumOptimizedTopDown(7));
