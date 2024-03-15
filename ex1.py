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
            self._insert_node(self.rootNode, data)

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

# Generate search tasks
def generate_search_tasks(num_tasks, list_size):
    # Generate random search tasks
    tasks = []
    original_list = list(range(list_size))
    for _ in range(num_tasks):
        shuffled_list = original_list.copy()
        random.shuffle(shuffled_list)
        tasks.append(shuffled_list)
    return tasks

# Measure performance
def measure_performance(search_tasks):
    # Measure the performance of the search tree for each search task
    performance_results = []

    for task in search_tasks:
        my_tree = SearchTree()
        for number in task:
            my_tree.add_node(number)

        total_search_time = 0
        for number in range(1000):
            _, search_time = my_tree.search(number)
            total_search_time += search_time

        average_search_time = total_search_time / 1000
        max_balance_value = my_tree.max_balance()
        performance_results.append((average_search_time, max_balance_value))

    return performance_results

# Example usage
search_tasks = generate_search_tasks(1000, 1000)
performance_results = measure_performance(search_tasks)

# Print the performance results for the first 5 tasks
for i in range(5):
    avg_time, max_balance = performance_results[i]
    print(f"Task {i + 1}: Average Search Time = {avg_time:.6f} seconds, Max Balance = {max_balance}")


# Extract absolute balance and search time from performance results
absolute_balances = [abs(result[1]) for result in performance_results]
search_times = [result[0] for result in performance_results]

# Create scatterplot
plt.figure(figsize=(8, 6))
plt.scatter(absolute_balances, search_times, alpha=0.5)
plt.title('Search Time vs. Absolute Balance')
plt.xlabel('Absolute Balance')
plt.ylabel('Search Time (seconds)')
plt.grid(True)
plt.show()