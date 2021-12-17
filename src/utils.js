const { customAlphabet } = require('nanoid');

const log = obj => {
  const util = require('util');
  console.log(util.inspect(obj, { showHidden: false, depth: null, colors: true }));
};

// [1, max]
const randInt = (max = 100) => Math.floor(Math.random() * max + 1);

// [min, max]
const randMinMax = (min = 0, max = 100) => min + Math.floor(Math.random() * (max + 1 - min));

const randArray = (length = 10, min = 1, max = 100) =>
  [...Array(length)].map(() => randMinMax(min, max));

const getShuffled = arr => {
  return arr
    .map(value => ({ value, sort: Math.random() }))
    .sort((a, b) => a.sort - b.sort)
    .map(({ value }) => value);
};

const randStr = (length = 8, allow_duplicate = false) => {
  const characterSpace = 'abcdefghijklmnopqrstuvwxyz';
  const str = allow_duplicate
    ? customAlphabet(characterSpace, 26)()
    : getShuffled(Array.from(characterSpace)).join('');
  return str.slice(0, length);
};

const doReps = (callback, number) => [...Array(number)].map(() => callback());

module.exports = {
  log,
  randInt,
  randMinMax,
  randArray,
  randStr,
  doReps,
};
