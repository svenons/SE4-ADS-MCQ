## 🧠 Open Question 1 – Recursion (10 points)

**Problem: Reverse a String Recursively**

Write a **recursive function** that takes a string `s` and returns it reversed.

### Example:
Input: `"algorithms"`  
Output: `"smhtirogla"`

### Requirements:
- No loops or built-in reverse functions.
- Clearly define base and recursive cases.
- Analyze the time and space complexity.

---

## 🌳 Open Question 2 – Binary Tree Tasks (15 points)

You are given a binary tree stored as a class structure:

"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""

### Tasks:
1. Write a recursive function to count all nodes **with exactly one child**.
2. Write a function to determine whether the tree is a **full binary tree** (every node has 0 or 2 children).
3. Provide a traversal (your choice) that demonstrates your implementation.
4. Discuss time complexity for your functions.

---

## 🔗 Open Question 3 – Graph Problem (15 points)

You are managing a delivery network. The nodes represent cities and the edges represent roads (with travel times):

```
Graph:
A —(3)— B
A —(5)— C
B —(1)— C
B —(4)— D
C —(2)— D
```

### Tasks:
1. Represent the graph as an **adjacency list with weights**.
2. Use **Dijkstra’s algorithm** to find the shortest path from A to D. Show step-by-step distance updates.
3. Write a function or pseudocode to reconstruct the shortest path from A to D.
4. Explain how adding a **negative weight** would affect Dijkstra's correctness.

---

## 🔧 Open Question 4 – Pseudocode Modification (10 points)

You are given pseudocode to compute the **maximum** in an array:

"""
function FindMax(A):
    max ← A[0]
    for i from 1 to length(A)-1:
        if A[i] > max:
            max ← A[i]
    return max
"""

### Tasks:
1. Modify the pseudocode so it **returns both the maximum value and its index**.
2. Describe how your version handles duplicate maximum values.
3. Does this change affect time or space complexity?