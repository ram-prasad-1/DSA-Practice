const { getShuffledArray } = require('./utils');
const { customAlphabet } = require('nanoid');

// [1, max]
const randInt = (max = 100) => Math.floor(Math.random() * max + 1);

// [min, max]
const randMinMax = (min = 0, max = 100) => min + Math.floor(Math.random() * (max + 1 - min));

const randArray = (length = 10, min = 1, max = 100) =>
  [...Array(length)].map(() => randMinMax(min, max));

const randStr = (length = 8, allow_duplicate = false) => {
  const characterSpace = 'abcdefghijklmnopqrstuvwxyz';
  const str = allow_duplicate
    ? customAlphabet(characterSpace, 26)()
    : getShuffledArray(Array.from(characterSpace)).join('');
  return str.slice(0, length);
};

module.exports = {
  randInt,
  randMinMax,
  randArray,
  randStr,
};
