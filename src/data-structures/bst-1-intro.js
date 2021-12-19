const { BaseBinarySearchTree, Node } = require('./helpers/base-bst');

`
Trick: Keep traversing to Left and right nodes if they are there. Return when node itself is null.

Tree Modification Trick: always return the same node and assign to the same node
`;

class BinarySearchTree extends BaseBinarySearchTree {
  constructor() {
    super();
    this.root = null;
  }

  addToArray(node, arr) {
    if (node === null) return;

    if (node.left) {
      this.addToArray(node.left, arr);
    }

    arr.push(node.value);

    if (node.right) {
      this.addToArray(node.right, arr);
    }
  }

  insert(newValue) {
    if (this.root === null) {
      this.root = new Node(newValue);
    } else {
      this._insert(this.root, newValue);
    }
  }

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

    if (value < currentNode.value) {
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

  _deleteNode(node, value) {
    if (node === null) return node;

    // traverse to the node
    if (value < node.value) {
      node.left = this._deleteNode(node.left, value);
    } else if (value > node.value) {
      node.right = this._deleteNode(node.right, value);
    } else {
      // this handles both single child and no child
      if (node.left === null) {
        // this works because we have received the node but returning its child
        return node.right;
      } else if (node.right === null) {
        return node.left;
      } else {
        // node with 2 children
        // get the value of inorder successor and then delete the successor.
        node.value = this.getNodeSmallestValue(node.right);
        node.right = this._deleteNode(node.right, node.value);
      }
    }

    return node;
  }

  getNodeSmallestValue(node) {
    let smallest = node.value;
    while (node.left != null) {
      smallest = node.left.value;
      node = node.left;
    }
    return smallest;
  }
}

module.exports = {
  BinarySearchTree,
  Node,
};
