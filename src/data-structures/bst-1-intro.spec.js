const { BinarySearchTree, Node } = require('./bst-1-intro');
const { randInt } = require('../utils/random');
const { doReps, log } = require('../utils/utils');

const items = [50, 32, 26, 42, 12, 7, 65, 79, 59, 84, 77];

it('should insert', function () {
  const bt = new BinarySearchTree();
  doReps(() => bt.insert(items.shift()), items.length);

  const arr = [];
  bt.preOrder(node => {
    arr.push(node.value);
  });
  console.log(arr);
});
