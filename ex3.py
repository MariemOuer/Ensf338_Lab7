
#AI declaration: used AI to fix up the code where it wasnt working specifically the rotate (right) and calling the tests


import random
import time
import matplotlib.pyplot as plt



class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# Define the AVL Tree class
class SearchTree:
    def __init__(self):
        self.root = None  #initialize the search tree

    def _height(self, node):
        if node is None:	#calauclare the height of the tree
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

    def _get_balance(self, node):
        if node is None:		#calculate the balance factor 
            return 0
        return self._height(node.left) - self._height(node.right)

    def _insert_node(self, currentNode, key):	#code from e2 
        if key < currentNode.key:
            if currentNode.left is None:
                currentNode.left = Node(key)
            else:
                self._insert_node(currentNode.left, key)
        elif key > currentNode.key:
            if currentNode.right is None:
                currentNode.right = Node(key)
            else:
                self._insert_node(currentNode.right, key)

    def insert(self, root, key):	#code from e2 
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self._height(root.left), self._height(root.right))

        balance = self._get_balance(root)

       
        if balance > 1 and key < root.left.key:
            print("Case #3a: adding a node to an outside subtree")  # Case 3a: Left-Left Case
            return self._right_rotate(root)

        
        if balance < -1 and key > root.right.key:
            print("Case 3b not supported") # Case 3b: Right-Right Case (not supported)
            return root

        return root

    def insert_wrapper(self, key):
        self.root = self.insert(self.root, key) 	#insert new key into the tree

    def _preorder(self, root):
        if root is not None:		#traverse the avl tree at the node in opposite order 
            print(root.key, end=" ")
            self._preorder(root.left)
            self._preorder(root.right)

    def call_preorder(self):
        self._preorder(self.root)       #call the preorfer function 
        print()

# Testing the AVL Tree implementation
if __name__ == "__main__":
    tree = SearchTree()

    # Test case for Case 3a
    keys_case_3a = [10, 20, 5]
    print("Testing Case 3a with keys:", keys_case_3a)
    for key in keys_case_3a:
        tree.insert_wrapper(key)
        tree.call_preorder()

    # Reset tree for the next test case
    tree = SearchTree()

    # Test case for Case 3b (not supported)
    keys_case_3b = [10, 5, 20]
    print("\nTesting Case 3b (not supported) with keys:", keys_case_3b)
    for key in keys_case_3b:
        tree.insert_wrapper(key)
        tree.call_preorder()