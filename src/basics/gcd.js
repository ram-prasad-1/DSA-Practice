
// gcd(a, b) = gcd(b, a%b)   if a > b
// gcd(a, b, c) = gcd(a, gcd(b, c))

function gcd(a, b) {
    if (b > a) [a, b] = [b, a];

    if (a % b === 0) return b;
    return gcd(b, a % b);
}
