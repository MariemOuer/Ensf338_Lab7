import random
import time
import matplotlib.pyplot as plt
    
#   binary search tree
class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def subtreeHeight(self):
        # Calculate the height  
        left_height = -1 if self.leftChild is None else self.leftChild.subtreeHeight()
        right_height = -1 if self.rightChild is None else self.rightChild.subtreeHeight()
        return 1 + max(left_height, right_height)

#  SearchTree  
class SearchTree:
    def __init__(self):
        self.rootNode = None

    def insert(self, data):
        # Insert a node with the specified data into the search tree
        if self.rootNode is None:
            self.rootNode = Node(data)
        else:
            self._insertNode(self.rootNode, data)

    def _insertNode(self, currentNode, data):
        #  recursively insert a node into the tree
        if data < currentNode.data:
            if currentNode.leftChild is None:
                currentNode.leftChild = Node(data)
            else:
                self._insertNode(currentNode.leftChild, data)
        elif data > currentNode.data:
            if currentNode.rightChild is None:
                currentNode.rightChild = Node(data)
            else:
                self._insertNode(currentNode.rightChild, data)
  #Ai decleration : Chatgbt used to aid in the fixing of the _searchRecursive , 
# _maxBalanceRecursive and measurePerformance functions.         
    def nodeBalance(self, node):
        # Calculate the balance factor of a node
        left_height = -1 if node.leftChild is None else node.leftChild.subtreeHeight()
        right_height = -1 if node.rightChild is None else node.rightChild.subtreeHeight()
        return left_height - right_height

    def search(self, data):
        # Search for a given data in the tree and measure the time taken
        start_time = time.time()
        found = self._searchRecursive(self.rootNode, data)
        end_time = time.time()
        return found, end_time - start_time

    def _searchRecursive(self, currentNode, data):
        #  recursively search for data in the tree
        if currentNode is None:
            return False
        if data == currentNode.data:
            return True
        elif data < currentNode.data:
            return self._searchRecursive(currentNode.leftChild, data)
        else:
            return self._searchRecursive(currentNode.rightChild, data)

    def maxBalance(self):
        #  maximum balance factor 
        _, maxBalance = self._maxBalanceRecursive(self.rootNode)
        return maxBalance

    def _maxBalanceRecursive(self, currentNode):
        # recursively find the maximum balance factor
        if currentNode is None:
            return None, 0

        _, left_maxBalance = self._maxBalanceRecursive(currentNode.leftChild)
        _, right_maxBalance = self._maxBalanceRecursive(currentNode.rightChild)

        current_balance = abs(self.nodeBalance(currentNode))
        maxBalance = max(current_balance, left_maxBalance, right_maxBalance)

        return currentNode, maxBalance

# random search tasks
def searchTasksGeneration(num_tasks, listSize):
    tasks = []
    original = list(range(listSize))
    for _ in range(num_tasks):
        shuffled = original.copy()
        random.shuffle(shuffled)
        tasks.append(shuffled)
    return tasks

#  performance of search tasks
def measurePerformance(searchTasks):
    performanceResults = []

    for task in searchTasks:
        myTree = SearchTree()
        for number in task:
            myTree.insert(number)

        averageSearchTime = 0
        for number in range(listSize):
            _, searchTime = myTree.search(number)
            averageSearchTime += searchTime

        averageTime = averageSearchTime / listSize
        maxBalance = myTree.maxBalance()
        performanceResults.append((averageTime, maxBalance))

    return performanceResults

# performance of search tasks
listSize = 1000
searchTasks = searchTasksGeneration(1000, listSize)
performanceResults = measurePerformance(searchTasks)

# scatterplot 
absoluteBalances = [abs(result[1]) for result in performanceResults]
searchTimes = [result[0] for result in performanceResults]
plt.figure(figsize=(8, 6))
plt.scatter(absoluteBalances, searchTimes, alpha=0.5)
plt.title('Search Time vs. Absolute Balance')
plt.xlabel('Absolute Balance')
plt.ylabel('Search Time (S)')
plt.grid(True)
plt.show()
