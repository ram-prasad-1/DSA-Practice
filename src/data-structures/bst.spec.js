const { BinarySearchTree, Node } = require('./bst');
const { doReps, log } = require('../utils/utils');

const intItems = [50, 32, 26, 42, 12, 65, 79, 59, 18, 84, 77];

it('should insert', function () {
  const bt = new BinarySearchTree();
  doReps(() => bt.insert(intItems.shift()), intItems.length);
  bt.prettyPrint();
  bt.deleteNode(65);
  // log(bt)
  bt.prettyPrint();
  // const arr = [];
  // bt.addToArray(bt.root, arr);
  // console.log(arr);

  // const arr = [];
  // bt.traverse(node => {
  //   arr.push(node.value);
  // });
  // log(bt);
  // console.log(arr);
});
