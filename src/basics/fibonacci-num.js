
`
F(n) = F(n-1) + F(n-2)
Time complexity: O(2^n) 
See: https://stackoverflow.com/a/45618079/3565194
`
function getFibNum(n) {
    if (n <= 1) return n;
    return getFibNum(n-1) + getFibNum(n-2)
}


console.log(getFibNum(7))