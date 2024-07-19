class Node {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  }
  
  const root = new Node('A');
  root.left = new Node('B');
  root.right = new Node('C');
  root.left.left = new Node('D');
  root.left.right = new Node('E');
  root.right.right = new Node('F');

  function depthFirstSearch(root, callback) {
    const stack = [];
    stack.push(root);
   
    while (stack.length) {
      const currentNode = stack.pop();
      callback(currentNode);
  
      if (currentNode.right) {
        stack.push(currentNode.right);      
      }
  
      if (currentNode.left) {
        stack.push(currentNode.left);     
      }
    }
  }

  depthFirstSearch(root, function(node) {
    console.log(node.value);
  });