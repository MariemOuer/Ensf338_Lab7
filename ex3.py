class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.weight = 0  

class SearchTree:
    def __init__(self):
        self.root = None #initialize the search tree

    def _height(self, node):
        if node is None: #calauclare the height of the tree
            return 0
        return node.height

    def _left_rotate(self, x):
        y = x.right     #perform the left rotation 
        t = y.left

        y.left = x
        x.right = t

        x.height = 1 + max(self._height(x.left), self._height(x.right)) #update the situation 
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def _right_rotate(self, y):
        x = y.left
        t = x.right     #perform the right rotation 

        x.right = y
        y.left = t

        y.height = 1 + max(self._height(y.left), self._height(y.right)) #update the situation 
        x.height = 1 + max(self._height(x.left), self._height(x.right))

        return x

    def _get_balance(self, node):
        if node is None:    #calculate the balance factor 
            return 0
        return self._height(node.left) - self._height(node.right)

    def _insert_node(self, currentNode, key):
        if key < currentNode.key:       #code from e2 
            if currentNode.left is None:
                currentNode.left = Node(key)
            else:
                self._insert_node(currentNode.left, key)
        elif key > currentNode.key:
            if currentNode.right is None:
                currentNode.right = Node(key)
            else:
                self._insert_node(currentNode.right, key)

    def _node_balance(self, node):
        if node is None:            #code from e2 
            return 0
        left_subtree_height = self._height(node.left) if node.left else -1
        right_subtree_height = self._height(node.right) if node.right else -1
        return left_subtree_height - right_subtree_height
    

    def insert(self, root, key):
        if root is None:        #insett a new node wth the key into the avl tree
            return Node(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self._height(root.left), self._height(root.right))    #update the height of the current node 

        balance = self._get_balance(root)       #check the balance factor 


        if balance > 1 and key < root.left.key: #case 3a 
            print("Case #3a: adding a node to an outside subtree")
            return self._right_rotate(root)
        
        elif balance < -1 and key > root.right.key:
            print("Case 3b not supported")
            return root  


    def insert_wrapper(self, key):                      #insert new key into the tree
        self.root = self.insert(self.root, key)

    def _preorder(self, root):
        if root is not None:        #traverse the avl tree at the node in opposite order 
            print(root.key, end=" ")
            self._preorder(root.left)
            self._preorder(root.right)

    def call_preorder(self):                 #call the preorfer function 
        self._preorder(self.root)

# Test
if __name__ == "__main__":
    tree = SearchTree()

    keys = [10, 20, 40, 30, 50, 25]  #new case for 
    print("Case 2 with this array: [10, 20, 40, 30, 50, 25] ")
    #keys = input("Enter an array:")    ---> tjos did not ework but i dont think we need to include a user input so its fine 
    for key in keys:
        tree.insert_wrapper(key)
        tree.call_preorder()
        print()
