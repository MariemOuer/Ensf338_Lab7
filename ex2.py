import random
import time
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def subtree_height(self):
        # Calculate the height of the subtree rooted at this node
        left_subtree_height = self.leftChild.subtree_height() if self.leftChild else -1
        right_subtree_height = self.rightChild.subtree_height() if self.rightChild else -1
        return 1 + max(left_subtree_height, right_subtree_height)

class SearchTree:
    def __init__(self):
        self.rootNode = None

    def add_node(self, data):
        # Add a node to the search tree
        if not self.rootNode:
            self.rootNode = Node(data)
        else:
            pivot, parent = self._find_pivot(data)
            if pivot is None:
                print("Case #1: Pivot not detected")
            else:
                if pivot == parent:
                    if data < pivot.data:
                        pivot.leftChild = Node(data)
                    else:
                        pivot.rightChild = Node(data)
                    self.update_balances(self.rootNode)
                else:
                    if parent is not None:  # Check if parent is not None
                        if pivot == parent.leftChild:
                            parent.leftChild = Node(data)
                        else:
                            parent.rightChild = Node(data)
                        self.update_balances(self.rootNode)
                    else:
                        print("Case #2: A pivot exists, and a node was added to the shorter subtree")
                        # Handle the case where parent is None
                        if data < pivot.data:
                            pivot.leftChild = Node(data)
                        else:
                            pivot.rightChild = Node(data)
                        self.update_balances(self.rootNode)


    def _find_pivot(self, data):
        # Find the pivot node for insertion
        parent = None
        current = self.rootNode

        while current:
            if data < current.data:
                if current.leftChild is None:
                    return current, parent
                parent = current
                current = current.leftChild
            elif data > current.data:
                if current.rightChild is None:
                    return current, parent
                parent = current
                current = current.rightChild
            else:
                return None, None  # Pivot not detected

        return None, None  # Pivot not detected

    def update_balances(self, node):
        # Update balances of nodes in the tree
        if node is not None:
            self.update_balances(node.leftChild)
            self.update_balances(node.rightChild)
            node_balance = self.node_balance(node)
            if abs(node_balance) > 1:
                print(f"Case #3 not supported for node {node.data}")

    # 
    def search(self, data):
        # Search for a given data in the tree and measure the time taken
        start_time = time.time()
        found = self._search_recursive(self.rootNode, data)
        end_time = time.time()
        return found, end_time - start_time

    def _search_recursive(self, currentNode, data):
        # Helper function to recursively search for data in the tree
        if currentNode is None:
            return False
        if data == currentNode.data:
            return True
        elif data < currentNode.data:
            return self._search_recursive(currentNode.leftChild, data)
        else:
            return self._search_recursive(currentNode.rightChild, data)
    
    def max_balance(self):
        # Find the maximum balance factor in the tree
        _, max_balance = self._max_balance_recursive(self.rootNode)
        return max_balance

    def _max_balance_recursive(self, currentNode):
        # Helper function to recursively find the maximum balance factor in the tree
        if currentNode is None:
            return None, 0

        _, left_max_balance = self._max_balance_recursive(currentNode.leftChild)
        _, right_max_balance = self._max_balance_recursive(currentNode.rightChild)

        current_balance = abs(self.node_balance(currentNode))
        max_balance = max(current_balance, left_max_balance, right_max_balance)

        return currentNode, max_balance

    def compute_balances(self):
        # Compute the balance factor for each node in the tree
        balances_list = []
        self._compute_balances_recursive(self.rootNode, balances_list)
        return balances_list   
    
    def _compute_balances_recursive(self, currentNode, balances_list):
        # Helper function to recursively compute balance factors for each node
        if currentNode is not None:
            balances_list.append((currentNode.data, self.node_balance(currentNode)))
            self._compute_balances_recursive(currentNode.leftChild, balances_list)
            self._compute_balances_recursive(currentNode.rightChild, balances_list)
    
    def _insert_node(self, currentNode, data):
        # Helper function to recursively insert a node into the tree
        if data < currentNode.data:
            if currentNode.leftChild is None:
                currentNode.leftChild = Node(data)
            else:
                self._insert_node(currentNode.leftChild, data)
        elif data > currentNode.data:
            if currentNode.rightChild is None:
                currentNode.rightChild = Node(data)
            else:
                self._insert_node(currentNode.rightChild, data)

    def node_balance(self, node):
        # Calculate the balance factor of a node (difference in heights of left and right subtrees)
        if node is None:
            return 0
        left_subtree_height = node.leftChild.subtree_height() if node.leftChild else -1
        right_subtree_height = node.rightChild.subtree_height() if node.rightChild else -1
        return left_subtree_height - right_subtree_height



# Test Cases
def test_cases():
    tree = SearchTree()
    print("Test Case 1:")
    tree.add_node(50)  # Adding a node results in case 1
    print("Test Case 2:")
    tree.add_node(25)  # Adding a node results in case 2
    print("Test Case 3:")
    tree.add_node(75)  # Adding a node results in case 3
    print("Test Case 4:")
    tree.add_node(60)  # Adding a node results in case 3

test_cases()
