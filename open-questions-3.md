## 🧠 Open Question 1 – Recursion (10 points)

**Problem: Digit Sum**

Write a recursive function that computes the sum of the digits of a non-negative integer `n`.

### Example:
Input: `n = 493`  
Output: `16` (4 + 9 + 3)

### Requirements:
- Use recursion.
- Clearly define the base and recursive cases.
- Explain how your function works.
- What is the time complexity with respect to the number of digits?

---

## 🌳 Open Question 2 – Binary Tree Tasks (15 points)

You are given a binary tree where each node contains an integer value:

```
        9
       / \
      3   11
         /  \
        10   15
```

### Tasks:
1. Write a function that returns the **maximum value** in the tree.
2. Write a function to check if the tree is a **valid Binary Search Tree**.
3. Write a recursive function that **sums all leaf node values**.
4. Briefly explain what would change in your traversal functions if the tree were a general (non-binary) tree.

---

## 🔗 Open Question 3 – Graph Problem (15 points)

You are given a **directed weighted graph**:

```
Vertices: A, B, C, D  
Edges: A→B (4), A→C (2), B→D (5), C→B (1), C→D (8)
```

### Tasks:
1. Draw the graph or describe its adjacency list with weights.
2. Trace Dijkstra’s algorithm starting from A. Show the shortest distances to each node.
3. Write pseudocode for Dijkstra’s algorithm using a priority queue.
4. If edge C→D had weight -2 instead, would Dijkstra still work? Explain.

---

## 🔧 Open Question 4 – Pseudocode Modification (10 points)

You are given pseudocode for a function that checks if a number is prime:

"""
function IsPrime(n):
    if n ≤ 1: return false
    for i from 2 to n−1:
        if n mod i == 0:
            return false
    return true
"""

### Tasks:
1. Modify the function to **reduce the time complexity** (e.g., avoid unnecessary checks).
2. Explain what change you made and why it improves performance.
3. What is the new time complexity?