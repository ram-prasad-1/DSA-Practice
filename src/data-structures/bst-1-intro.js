`

`;

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

  // trick: start with plain slate. now insert existing with new one as well.
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

  prettyPrint() {
    const trioArray = this.getTrioPerNodes();
    if (trioArray.length === 0) {
      console.log(null);
    }

    let rootIndex = -1;
    for (const [index, trio] of trioArray.entries()) {
      trio[0] = trio[0] || ' ';
      trio[2] = trio[2] || ' ';

      if (this.root.value === trio[1]) {
        rootIndex = index;
      }
    }

    const PADDING = 8;
    const TRIO_LENGTH = 10;
    const getSpaces = count => [...Array(count)].map(() => ' ').join('');
    const withFilledSpaces = trioStr => {
      if (trioStr.length < TRIO_LENGTH) {
        trioStr += getSpaces(TRIO_LENGTH - trioStr.length);
      }
      return trioStr;
    };

    let left = rootIndex - 1;
    let right = rootIndex + 1;

    let str =
      getSpaces(PADDING) + withFilledSpaces(`[${trioArray[rootIndex]}]`) + getSpaces(PADDING);
    let rowStr = '';

    while (left >= 0 || right < trioArray.length) {
      if (left >= 0) {
        rowStr = withFilledSpaces(`[${trioArray[left]}]`);
        left -= 1;
      }
      rowStr += getSpaces(PADDING);
      if (right < trioArray.length) {
        rowStr += withFilledSpaces(`[${trioArray[right]}]`);
        right += 1;
      }

      str += '\n' + rowStr;
    }

    console.log(str);
  }

  getTrioPerNodes() {
    const trioArray = [];
    this._getTrioPerNodes(this.root, trioArray);
    trioArray.sort((a, b) => {
      if (trioArray.length <= 1) {
        return 1;
      }
      return a[1] - b[1];
    });
    return trioArray;
  }

  _getTrioPerNodes(node, arr) {
    if (node === null) return null;
    const trio = [null, null, null];

    if (node.left) {
      trio[0] = this._getTrioPerNodes(node.left, arr);
    }

    trio[1] = node.value;

    if (node.right) {
      trio[2] = this._getTrioPerNodes(node.right, arr);
    }
    if (node.left !== null || node.right !== null) {
      arr.push(trio);
    }
    return node.value;
  }

  deleteNode(value) {
    this._deleteNode(this.root, value);
  }

  _deleteNode(node, value) {}
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
