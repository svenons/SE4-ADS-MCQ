## 🧠 Open Question 1 – Recursion (10 points)

**Problem: Sum of Even Squares**

Write a recursive function that, given a positive integer `n`, returns the sum of the squares of all even numbers from 1 to `n`.

### Example:
Input: `n = 6`  
Output: `56` (2² + 4² + 6² = 4 + 16 + 36 = 56)

### Requirements:
- Use recursion (no loops or built-in functions).
- Clearly define the base case and the recursive case.
- Explain how the function works and provide its time complexity.

---

## 🌳 Open Question 2 – Binary Tree Tasks (15 points)

Given the following binary tree:

```
        15
       /  \
      10   20
     / \   / \
    8  12 17 25
```

### Tasks:
1. Write a function to perform **level-order traversal** of this tree.
2. Modify the tree into a **mirror image** (swap left and right children recursively).
3. After mirroring, list the **inorder traversal** of the tree.
4. Explain whether the mirrored tree is still a **Binary Search Tree**, and why or why not.

---

## 🔗 Open Question 3 – Graph Problem (15 points)

You are given the following undirected graph represented as an adjacency list:

```
A: [B, C]
B: [A, D]
C: [A, D]
D: [B, C, E]
E: [D]
```

### Tasks:
1. Perform a **Breadth-First Search (BFS)** starting from node A. Show the order of traversal.
2. Write pseudocode to implement BFS using a queue.
3. Identify if the graph contains a **cycle**, and explain how you determine that.
4. If this were a **directed graph**, would your answer to (3) change? Explain.

---

## 🔧 Open Question 4 – Pseudocode Modification (10 points)

You are given pseudocode that performs **insertion sort**:

"""
function InsertionSort(A):
    for i from 1 to length(A)-1:
        key ← A[i]
        j ← i - 1
        while j ≥ 0 and A[j] > key:
            A[j+1] ← A[j]
            j ← j - 1
        A[j+1] ← key
"""

**Task**: Modify this pseudocode to sort the array in **descending order**.

### Additional:
- Provide the modified pseudocode.
- Briefly explain what you changed.
- Does the time complexity change? Why or why not?