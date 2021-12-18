const { BinarySearchTree, Node } = require('./bst-1-intro');
const { randInt } = require('../utils/random');
const { doReps, log, popStart } = require('../utils/utils');

const data = [38, 20, 13, 94, 26, 51, 67, 48, 11, 72];

const bt = new BinarySearchTree(popStart(data));
doReps(() => bt.insert(randInt()), 4);
log(bt);
console.log(`${bt}`);
