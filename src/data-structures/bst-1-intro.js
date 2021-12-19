const { BaseBinarySearchTree, Node } = require('./helpers/base-bst');

class BinarySearchTree extends BaseBinarySearchTree {
  constructor() {
    super();
    this.root = null;
  }

  insert(newValue) {
    if (this.root === null) {
      this.root = new Node(newValue);
    } else {
      this._insert(this.root, newValue);
    }
  }

  // trick: start with plain slate. now insert existing with new one as well.
  _insert(node, newValue) {
    if (node === null) {
      return new Node(newValue);
    }

    if (newValue <= node.value) {
      node.left = this._insert(node.left, newValue);
    } else {
      node.right = this._insert(node.right, newValue);
    }
    return node;
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

  traverse(operation) {
    this._inOrder(this.root, operation);
  }

  _inOrder(node, operation) {
    if (node === null) {
      return;
    }
    this._inOrder(node.left, operation);
    // for preOrder, move operation above and so on
    operation(node);
    this._inOrder(node.right, operation);
  }

  bfsTraverse(nodeOp) {
    if (this.root === null) return;
    const queue = [this.root];

    while (queue.length !== 0) {
      // dequeue
      const current = queue.shift();
      nodeOp(current);
      // enqueue
      current.left && queue.push(current.left);
      current.right && queue.push(current.right);
    }
  }

  deleteNode(value) {
    this._deleteNode(this.root, value);
  }

  _deleteNode(node, value) {}
}

module.exports = {
  BinarySearchTree,
  Node,
};
