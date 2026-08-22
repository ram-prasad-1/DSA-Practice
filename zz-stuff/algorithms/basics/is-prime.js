`
Prime Numbers: 2, 3, 5, 7, ...
All prime numbers take the form of 6k±1, for ∀ k >= 1
`;
function isPrime(n) {
  if (n <= 1) return false;
  if (n <= 3) return true;
  if (n % 2 === 0 || n % 3 === 0) return false;

  for (let i = 1; (6 * i + 1) * (6 * i + 1) <= n; i++) {
    if (n % (6 * i - 1) === 0 || n % (6 * i + 1) === 0) return false;
  }

  return true;
}
