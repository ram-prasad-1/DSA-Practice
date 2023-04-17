// I/P => O/P
// 1234 => ONE THOUSAND TWO HUNDRED THIRTY FOUR
// 123456 => ONE LAKH TWENTY THREE THOUSAND FOUR HUNDRED FIFTY SIX
// 12345678 => ONE CRORE TWENTY THREE LAKH FORTY FIVE THOUSAND SIX HUNDRED SEVENTY EIGHT

// Limit: 99999999

const toWord = {
  0: 'zero',
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety',
};

function hundToWord(num) {
  if (num <= 20) {
    return toWord[num];
  }

  const f = ('' + num)[0];
  let word = toWord[+f * 10];

  const s = ('' + num)[1];
  word += ' ' + toWord[s];

  return word;
}

function getNumInWords(n) {
  let num = '' + n;

  let currLen = num.length;

  let res = '';

  while (currLen > 0) {
    if (currLen >= 8) {
      res += toWord[num[0]] + ' ' + 'Crore ';
      num = num.slice(1);
      currLen = 7;
    } else if (currLen >= 6) {
      let pick = 1;
      if (currLen === 7) {
        pick = 2;
      }
      const t = +num.slice(0, pick);

      res += hundToWord(t) + ' ' + 'Lakh ';

      num = num.slice(pick);
      currLen = 5;
    } else if (currLen >= 4) {
      let pick = 1;
      if (currLen === 5) {
        pick = 2;
      }
      const t = +num.slice(0, pick);
      res += hundToWord(t) + ' ' + 'Thousand ';

      num = num.slice(pick);
      currLen = 3;
    } else if (currLen === 3) {
      let pick = 1;
      const t = +num.slice(0, pick);
      res += toWord[t] + ' ' + 'Hundred ';

      num = num.slice(pick);
      currLen = 2;
    } else {
      const t = +num;
      res += hundToWord(t);

      currLen = 0;
    }
  }

  return res;
}

console.log(getNumInWords(12345678));
console.log(getNumInWords(900516));
console.log(getNumInWords(10000));
console.log(getNumInWords(350006));
