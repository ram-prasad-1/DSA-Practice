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
  let current = 1;
  let prev = 1;
  let prevToPrev = 1;
  for (let i = 3; i <= n; i++) {
    current = prev + prevToPrev;
    prevToPrev = prev;
    prev = current;
  }

  return current;
}

function getFibNumOptimizedTopDown(n, cache = {}) {
  if (n === 1 || n === 2) return 1;

  if (!cache[n]) {
    cache[n] = getFibNumOptimizedTopDown(n - 1, cache) + getFibNumOptimizedTopDown(n - 2, cache);
  }

  return cache[n];
}

console.log(getFibNumOptimized(7) === getFibNum(7), getFibNumOptimized(7), getFibNum(7));
