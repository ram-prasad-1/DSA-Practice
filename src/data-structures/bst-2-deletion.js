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
    }

    if (newValue <= currentNode.value) {
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
      return null;
    }
    if (value === currentNode.value) {
      return currentNode;
    }

    if (value <= currentNode.value) {
      return this._search(currentNode.left, value);
    } else {
      return this._search(currentNode.right, value);
    }
  }
}

module.exports = {
  Node,
  BinarySearchTree,
};
