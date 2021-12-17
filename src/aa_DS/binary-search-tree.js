const { randArray } = require('../utils');
const { doTimes } = require('../utils');
const { randInt, log } = require('../utils');

class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BinarySearchTree {
  constructor(rootValue) {
    this.root = new Node(rootValue);
  }

  insert(newValue) {
    this._insert(this.root, newValue);
  }

  _insert(currentNode, newValue) {
    if (currentNode === null) {
      return new Node(newValue);
    } else if (newValue <= currentNode.value) {
      currentNode.left = this._insert(currentNode.left, newValue);
    } else {
      currentNode.right = this._insert(currentNode.right, newValue);
    }
    return currentNode;
  }

  search(value) {
    return this._search(this.root, value);
  }

  _search(currentNode, value) {
    if (currentNode == null) {
      return false;
    }
    if (value === currentNode.value) {
      return true;
    }

    if (value <= currentNode.value) {
      return this._search(currentNode.left, value);
    } else {
      return this._search(currentNode.right, value);
    }
  }
}

const bt = new BinarySearchTree(randInt());

doTimes(() => bt.insert(randInt()), 5);
log(bt);
