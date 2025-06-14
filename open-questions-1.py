# EX1

def climbstairs(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climbstairs(n-1) + climbstairs(n-2) + climbstairs(n-3)
    
print(climbstairs(4))
print(climbstairs(5))
print(climbstairs(6))

## Exercise 2

#2.1

# inorder: (Left → Root → Right)
[2, 4, 6, 7, 10, 12]
# Start at root: 7
# Go left to 4 → go left to 2 → no children → visit 2
# Back to 4 → visit 4 → go right to 6 → no children → visit 6
# Back to 7 → visit 7
# Go right to 10 → no left child → visit 10 → go right to 12 → visit 12

#preorder (Root → Left → Right)
[7, 4, 2, 6, 10, 12]
# Start at root: 7 → visit 7
# Go left to 4 → visit 4
# Go left to 2 → visit 2 → back to 4
# Go right to 6 → visit 6 → back to 7
# Go right to 10 → visit 10
# Go right to 12 → visit 12

#postorder (Left → Right → Root)
[2, 6, 4, 12, 10, 7] 
# Go left to 4
# Go left to 2 → visit 2
# Back to 4 → go right to 6 → visit 6
# Back to 4 → visit 4
# Back to 7 → go right to 10
# No left child → go right to 12 → visit 12
# Back to 10 → visit 10
# Back to 7 → visit 7

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
# Build tree:
#         7
#        / \
#       4   10
#      / \    \
#     2   6    12

root = Node(7)
root.left = Node(4)
root.right = Node(10)
root.left.left = Node(2)
root.left.right = Node(6)
root.right.right = Node(12)

#2.2
def height(root):
    if root is None:
        return -1  # or return 0 if you define a single node tree as height 1
    return 1 + max(height(root.left), height(root.right))
print("Height of the tree: ", height(root))

#2.3
def leafnodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return 0 + leafnodes(root.left) + leafnodes(root.right)
print("Leafnodes: ", leafnodes(root))

#2.4 This is a BST because on the right of any node all the variables are higher than it, and on the left of any node they are lower.

## Exercise 3.1 & 3.2
array = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": ["E"],
    "E": []
}

from collections import defaultdict

def all_topo_sorts(graph):
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    visited = set()
    all_orders = []

    def dfs(path):
        flag = False
        for node in graph:
            if node not in visited and in_degree[node] == 0:
                # Choose this node
                visited.add(node)
                path.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1

                dfs(path)

                # Backtrack
                visited.remove(node)
                path.pop()
                for neighbor in graph[node]:
                    in_degree[neighbor] += 1
                flag = True

        if not flag and len(path) == len(graph):
            all_orders.append(path[:])

    dfs([])
    return all_orders

# Graph input
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": ["E"],
    "E": []
}

# Get all topological orderings
orders = all_topo_sorts(graph)

# Print them
for i, order in enumerate(orders, 1):
    print(f"Order {i}: {order}")

# 3.4 It helps systems find a valid execution order of tasks.

## Exercise 4
"""
function BinarySearch(A, target):
    left ← 0
    right ← length(A) - 1
    result ← -1

    while left ≤ right:
        mid ← (left + right) // 2

        if A[mid] == target:
            result ← mid         // store the match
            right ← mid - 1       // continue searching left

        else if A[mid] < target:
            left ← mid + 1

        else:
            right ← mid - 1

    return result
"""

# This works because there is a results variable that stores index and gets overwritten if any other variable to the left of it is found. 
# Time complexity isn't affected too much as we are just searching from the left of the found array, so it should still be O(logn) as worst case.