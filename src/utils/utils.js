const log = obj => {
  const util = require('util');
  console.log(util.inspect(obj, { showHidden: false, depth: null, colors: true }));
};

const getShuffledArray = arr => {
  return arr
    .map(value => ({ value, sort: Math.random() }))
    .sort((a, b) => a.sort - b.sort)
    .map(({ value }) => value);
};

const doReps = (callback, number) => [...Array(number)].map(() => callback());

module.exports = {
  log,
  doReps,
  getShuffledArray,
};
