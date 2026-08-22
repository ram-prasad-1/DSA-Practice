`
  given a, b there exists 2 integers x and y such that: ax + by = gcd(a,b)
  https://brilliant.org/wiki/extended-euclidean-algorithm/
  https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
`;

function gcdExtended(a, b) {
  // Trick: gcd = the last non-zero remainder
  if (b === 0) return [a, 0, 1];

  const [gcd, x, y] = gcdExtended(b, a % b);
  return [gcd, y - Math.floor(a / b) * x, x]
}

console.log(gcdExtended(18, 60))
