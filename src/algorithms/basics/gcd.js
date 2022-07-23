`
  gcd(a, b) = gcd(b, a%b)
  Trick: Assume a > b

  gcd(a, b, c) = gcd(a, gcd(b, c))
`;

function gcd(a, b) {
  // Trick: gcd = the last non-zero remainder
  if (b === 0) return a;
  return gcd(b, a % b);
}
