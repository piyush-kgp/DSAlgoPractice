
class TreeNode:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

    def insertNode(self, val):
        if not self.val:
            self.val = val
            print('Inserted %s at %s ie Root' %(val, self))
        elif val <= self.val:
            if not self.left:
                self.left = TreeNode(val)
                print('Inseted %s at %s ie Left' %(val, self.left))
            else:
                self.left.insertNode(val)
        else:
            if not self.right:
                self.right = TreeNode(val)
                print('Inserted %s at %s ie Right' %(val, self.right))
            else:
                self.right.insertNode(val)

    def printTree(self):
        if self.left:
            self.left.printTree()
        print('%s at %s' %(self.val, self))
        if self.right:
            self.right.printTree()

    def traverseTree(self, root):
        A = []
        if root:
            A = self.traverseTree(root.left)
            A.append(root.val)
            A.extend(self.traverseTree(root.right))
        return A

if __name__ == '__main__':
    import random
    myTree = TreeNode()
    for _ in range(10):
        myTree.insertNode(random.randint(1, 100))
    myTree.printTree()
    print(myTree.traverseTree(myTree))
