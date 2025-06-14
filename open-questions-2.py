#Exercise 1

def squaresum(n) -> int:
    if n == 0:
        return 0
    if n % 2 == 1:
        return squaresum(n-1)
    else:
        return squaresum(n-1)+n*n
    
print(squaresum(6))

# Exercise 2

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def traverse(root, level=0):
    result = []
    def dfs(node, local_level=0):
        if node is None:
            return
        if local_level == level:
            result.append(node.val)
        else:
            dfs(node.left, local_level + 1)
            dfs(node.right, local_level + 1)
    dfs(root)
    return result

root = Node(15)
root.left = Node(10)
root.left.left = Node(8)
root.left.right = Node(12)
root.right = Node(20)
root.right.right = Node(25)
root.right.left = Node(17)

print(traverse(root, 2)) # [8, 12, 17, 25]

# Exc. 2.2

"""
        15
       /  \
      20   10
     / \   / \
    25  17 12 8
"""

# Inorder traversal would be [25, 20, 17, 15, 10, 12, 8]

# Its not a BST obviously, cause Node > node.right, and Node < node.left

## Exercise 3

"""
A -> frontier [B, C], visited [A]
B -> [C, D], visited [A, B]
C -> [D], visited [A,B,C]
D -> [E], visited [A,B,C,D]
E -> [], visited [A,B,C,D,E]
"""

"""
Ex.3.2

BFS(node):
    create empty queue Q
    create empty list Visited

    enqueue node into Q
    add node to Visited

    while Q is not empty:
        current = Q.dequeue()
        process current

        for each neighbor in current.neighbours:
            if neighbor not in Visited:
                enqueue neighbor into Q
                add neighbor to Visited
"""

# 3.3. The graph contains many cycles, which is why BFS would need implementation of the visited, not to loop forever.

# 3.4. If it was a directed graph, there still could be cycles and looping would still be possible, just in one direction.

# Exercise 4

"""
function InsertionSort(A):
    for i from 1 to length(A)-1:
        key ← A[i]
        j ← i - 1
        while j ≥ 0 and A[j] < key:
            A[j+1] ← A[j]
            j ← j - 1
        A[j+1] ← key
"""
#Changed A[j] > key to A[j] < key, this makes bigger elements rise to the top = descending
# It does not change the time complexity at all