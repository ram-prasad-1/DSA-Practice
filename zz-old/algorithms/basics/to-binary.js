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

function toDecimal(binary) {
  let result = 0;
  let i = binary.length - 1;
  while (i >= 0) {
    result += Math.pow(2, binary.length - 1 - i) * +binary[i];
    i -= 1;
  }
  return result;
}

console.log(toDecimal('1111'));
