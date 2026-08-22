function parse(str) {
  return _parse(str.replaceAll(' ', ''));
}

// parse('[]') // []
// parse('[1, 2]') // [1, 2]
// parse('[1, [2, 4], 3]') // [1, [2], 3]

// Trick: Replace the deepest array with a Symbol primitive

function _parse(inputStr) {
  let str = inputStr.slice(1, inputStr.length - 1);
  const stack = [];

  let current = '';
  let i = 0;
  while (i < str.length) {
    if (str[i] === ',') {
      stack.push(current);
      current = '';
      i++;
    } else if (str[i] === '[') {
      let t = null;
      let temp = str;
      while (temp.indexOf('[') >= 0 && temp.indexOf('[') < temp.indexOf(']')) {
        temp = temp.slice();
      }
      // const t = str.indexOf(']')
      const newStr = str.slice(i, t + 1);
      current = _parse(newStr);
      stack.push(current);
      current = '';
      str = str.slice(t + 2);
      i = 0;
    } else {
      current += str[i];
      i++;
    }
  }
  current && stack.push(current);
  return stack;
}

// console.log(parse('[1, 2]'));
// console.log(parse('[]'));

console.log(parse('[1, [2, 4], 3]'));
