const { BinarySearchTree, Node } = require('./bst-1-intro');
const { intItems } = require('../utils/data');
const { doReps, log } = require('../utils/utils');

it('should insert', function () {
  const bt = new BinarySearchTree();
  doReps(() => bt.insert(intItems.shift()), intItems.length);

  const arr = [];
  bt.traverse(node => {
    arr.push(node.value);
  });
  console.log(arr);
});
