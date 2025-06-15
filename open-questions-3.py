# Exercise 1

def sumOfDigits(n):
    if n is None:
        return
    if len(str(n)) == 1:
        return n
    else:
        return int(str(n)[:1]) + sumOfDigits(int(str(n)[1:]))
    
print(sumOfDigits(493))
# Time complexity could be O(amount of digits)?

#Exercise 2

"""
        9
       / \
      3   11
         /  \
        10   15
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    
root = Node(9)
root.left = Node(3)
root.right = Node(11)
root.right.right = Node(15)
root.right.left = Node(10)

def findMaxValue(node):
    while node.right is not None:
        node = node.right
    return node.value
    
print(findMaxValue(root))

def isValidBinarySearch(node):
    if node is None:
        return
    if not node.right is None:
        if node.right.value < node.value:
            return False
    if not node.left is None:
        if node.left.value > node.value:
            return False
    isValidBinarySearch(node.left)
    isValidBinarySearch(node.right)
    return True

print(isValidBinarySearch(root))

def countLeafNodeValues(node):
    if node is None:
        return
    if node.right is None and node.left is None:
        return node.value
    return countLeafNodeValues(node.right) + countLeafNodeValues(node.left)

print(countLeafNodeValues(root))

# Ex. 2.4 If the tree were not a binary tree, then none of the functions would work, because left childs value would not be necessarily smaller then the root value, same with right child.

## Exercise 3

array = {
    "A": {"B": 4, "C": 2},
    "B": {"D": 5},
    "C": {"B": 1, "D": 8},
    "D": {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    while len(visited) < len(graph):
        #select the unvisited node with the smallest distance
        current_node = None
        for node in graph:
            if node not in visited:
                if current_node is None or distances[node] < distances[current_node]:
                    current_node = node

        if current_node is None:
            break  # all remaining nodes are inaccessible from start

        #update the distances to neighbors
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

        visited.add(current_node)

    return distances

print(dijkstra(array, "A"))
"""
The Dijkstra’s algorithm at first has two arrays:
- unvisited = {'A', 'B', 'C', 'D'}
- distances = {'A': 0, 'B': inf, 'C': inf, 'D': inf}

Start from node A:
  - A has neighbors B (4) and C (2)
  - So:
    distances = {'A': 0, 'B': 4, 'C': 2, 'D': inf}
    unvisited = {'B', 'C', 'D'}

Next pick the unvisited node with the smallest distance → C (2)
  - C has neighbors B (1) and D (8)
  - New distance to B: 2 + 1 = 3 → update B (was 4)
  - New distance to D: 2 + 8 = 10
  - Now:
    distances = {'A': 0, 'B': 3, 'C': 2, 'D': 10}
    unvisited = {'B', 'D'}

Next pick the smallest unvisited node → B (3)
  - B has neighbor D (5)
  - New distance to D: 3 + 5 = 8 → update D (was 10)
  - Now:
    distances = {'A': 0, 'B': 3, 'C': 2, 'D': 8}
    unvisited = {'D'}

Next pick D (8)
  - D has no neighbors
  - unvisited = {}

All nodes visited, done.

Final distances:
{'A': 0, 'B': 3, 'C': 2, 'D': 8}
"""

#3.4. No, because Dijkstra is a greedy algorithm and assumption is that a distance can't improve later.
# It only works on non-negative edge weights.

## Exercise 4

"""
function IsPrime(n):
    if n ≤ 1: return false
    if n == 2: return true
    if n mod 2 == 0: return false
    for i from 3 to rounddown(sqrt(n)) step 2: #rounding is sometimes also refered as floor (to get the whole number)
        if n mod i == 0:
            return false
    return true
"""

# After confirming n isn’t even (n mod 2 != 0), we only check odd divisors starting from 3.
# new time complexity is square root of n