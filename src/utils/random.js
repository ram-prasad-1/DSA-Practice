const { customAlphabet } = require('nanoid');

`
Others:
faker.lorem.slug(3)
faker.datatype.number()
`;

// [min, max]
const randInt = (options = 99) => {
  if (typeof options === 'number') {
    options = {
      min: 0,
      max: options,
    };
  }
  return _randMinMax(options);
};

const _randMinMax = options => {
  const { min, max } = options;
  return min + Math.floor(Math.random() * (max + 1 - min));
};

const randIntArray = (length = 10, options = { min: 0, max: 99 }) =>
  [...Array(length)].map(() => randInt(options));

const randStr = (length = 8, allow_duplicate = false) => {
  // import here to avoid circular dependency
  const { getShuffledArray } = require('./utils');
  const characterSpace = 'abcdefghijklmnopqrstuvwxyz';
  const str = allow_duplicate
    ? customAlphabet(characterSpace, 26)()
    : getShuffledArray(Array.from(characterSpace)).join('');
  return str.slice(0, length);
};

module.exports = {
  randInt,
  randIntArray,
  randStr,
};
