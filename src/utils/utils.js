const { randInt } = require('./random');

const log = obj => {
  const util = require('util');
  console.log(util.inspect(obj, { showHidden: false, depth: null, colors: true }));
};

const doReps = (callback, number) => [...Array(number)].map(() => callback());

const popRandom = arr => {
  if (arr.length === 0) return null;
  const index = randInt() % arr.length;
  const value = arr[index];
  arr.splice(index, 1);
  return value;
};

const getShuffledArray = arr => {
  return arr
    .map(value => ({ value, sort: Math.random() }))
    .sort((a, b) => a.sort - b.sort)
    .map(({ value }) => value);
};

module.exports = {
  log,
  doReps,
  getShuffledArray,
  popRandom,
};
