class BinarySearchTree {
  constructor() {
    this.root = null;
  }

  insert(newValue) {
    if (this.root === null) {
      this.root = new Node(newValue);
    } else {
      this._insert(this.root, newValue);
    }
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

  traverse(nodeOperation) {
    this._inOrder(this.root, nodeOperation);
  }

  _inOrder(node, nodeOperation) {
    if (node === null) {
      return;
    }
    this._inOrder(node.left, nodeOperation);
    // for preOrder, move nodeOperation above and so on
    nodeOperation(node);
    this._inOrder(node.right, nodeOperation);
  }
}

class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

module.exports = {
  Node,
  BinarySearchTree,
};
