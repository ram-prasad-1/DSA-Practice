// Trick: Continue while loop till the number becomes 0
function toBinary(n) {
  let result = '';
  let x = n;
  while (x !== 0) {
    result = `${x % 2}${result}`;
    x = Math.trunc(x / 2);
  }
  return result;
}
