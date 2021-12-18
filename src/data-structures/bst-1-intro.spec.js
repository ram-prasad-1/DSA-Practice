const { BinarySearchTree, Node } = require('./bst-1-intro');
const { randInt } = require('../utils/random');
const { doReps, log, popStart } = require('../utils/utils');

const data = [38, 20, 13, 94, 26, 51, 67, 48, 11, 72];

it('should insert', function () {
  const bt = new BinarySearchTree(popStart(data));
  doReps(() => bt.insert(popStart(data)), 4);
  // log(bt);
  console.log(`${bt}`);
});
