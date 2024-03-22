
#much of the code was used from ex3 
#AI declaration: it was used to clean up the code and fix the calling text functions 

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _left_rotate(self, x):
        y = x.right
        t = y.left		#perform the left rotation

        y.left = x
        x.right = t

        x.height = 1 + max(self._height(x.left), self._height(x.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def _right_rotate(self, y):
        x = y.left
        t = x.right		#perform the right rotation 

        x.right = y
        y.left = t

        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))

        return x

    def _lr_rotate(self, z):
        z.left = self._left_rotate(z.left)
        return self._right_rotate(z)

    def _rl_rotate(self, z):
        z.right = self._right_rotate(z.right)
        return self._left_rotate(z)

    def _get_balance(self, node):
        if node is None:    #cbalce the cnodes 
            return 0
        return self._height(node.left) - self._height(node.right)

    def insert(self, root, key):
        if root is None:  
            return Node(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self._height(root.left), self._height(root.right))

        balance = self._get_balance(root)

       
        if balance > 1 and key < root.left.key: #case 3a 
            print("Case #3a: adding a node to an outside subtree")
            return self._right_rotate(root)
        
        
        if balance > 1 and key > root.left.key:  #case 3b
            print("Case #3b: adding a node to an inside subtree, performing LR rotation")
            return self._lr_rotate(root)

        return root

    def insert_wrapper(self, key):
        self.root = self.insert(self.root, key)

    def _preorder(self, root):
        if root is not None:
            print(root.key, end=" ")
            self._preorder(root.left)
            self._preorder(root.right)

    def preorder(self):
        self._preorder(self.root)
        print()

# Testing the AVL Tree implementation
if __name__ == "__main__":
    # Test Case 1 for Case 3b
    tree1 = AVLTree()
    keys1 = [30, 20, 40, 35, 50, 45]  # Triggers LR rotation
    print("Test Case 1 for Case 3b:")
    for key in keys1:
        tree1.insert_wrapper(key)
        tree1.preorder()

    # Test Case 2 for Case 3b
    tree2 = AVLTree()
    keys2 = [30, 40, 20, 25]  # Another scenario triggering LR rotation
    print("\nTest Case 2 for Case 3b:")
    for key in keys2:
        tree2.insert_wrapper(key)
        tree2.preorder()