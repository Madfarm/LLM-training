class Node {
    constructor(public value: string) {
      this.left = null;
      this.right = null;
    }
    left: Node | null;
    right: Node | null;
  }
  
  function depthFirstSearch(root: Node | null, callback: (node: Node) => void): void {
    if (!root) {
     return;
    }
    const stack: Node[] = [];
    stack.push(root);
  
    while (stack.length) {
      const currentNode = stack.pop()!;
  
      callback(currentNode);
  
      if (currentNode.right) {
        stack.push(currentNode.right);
      }
  
      if (currentNode.left) {
        stack.push(currentNode.left);   
      }
    } 
  }
  
  
  // Example usage
  const root = new Node('A');
  root.left = new Node('B');
  root.right = new Node('C');
  root.left.left = new Node('D');
  root.left.right = new Node('E');
  root.right.right = new Node('F');
  
  // Printing the node values during DFS traversal
  depthFirstSearch(root, (node) => {
    console.log(node.value);
  });