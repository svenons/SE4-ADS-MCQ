## 🧠 Open Question 1 – Recursion (10 points)

**Problem: Count Ways to Climb Stairs**

You are climbing a staircase with `n` steps. You can climb either 1, 2, or 3 steps at a time. Write a **recursive algorithm** to compute the number of distinct ways to reach the top.

### Requirements:
- Clearly define base cases.
- Write your function using either pseudocode or any programming language.
- You are **not allowed** to use memoization or iterative solutions.
- Explain how your recursion works and analyze its time complexity.

### Example:
Input: `n = 4`  
Output: `7` (ways: 1-1-1-1, 1-1-2, 1-2-1, 2-1-1, 2-2, 3-1, 1-3)
---

## 🌳 Open Question 2 – Binary Tree Tasks (15 points)

Given the following binary tree:

```
        7
       / \
      4   10
     / \    \
    2   6    12
```

### Tasks:
1. Perform **inorder**, **preorder**, and **postorder** traversals. Write the sequence of values visited.
2. Write a function to compute the **height** of the tree.
3. Write a function to **count the number of leaf nodes**.
4. Describe whether this is a **Binary Search Tree**, and why.

Use pseudocode or any language. Clearly explain your reasoning and structure your answers.

---

## 🔗 Open Question 3 – Graph Problem (15 points)

You are given a directed acyclic graph (DAG) representing task dependencies:

- Task A must be done before B and C.
- Task B must be done before D.
- Task C must be done before D.
- Task D must be done before E.

### Tasks:
1. Draw the graph or describe its **adjacency list**.
2. Perform a **topological sort** (list all valid orders).
3. Write pseudocode or a function to **implement topological sorting** using **DFS**.
4. Explain how topological sorting is used in **project scheduling**.

---

## 🔧 Open Question 4 – Pseudocode Modification (10 points)

You are given the following pseudocode that searches for an element in a **sorted array** using binary search:

"""
function BinarySearch(A, target):
    left ← 0
    right ← length(A) - 1
    while left ≤ right:
        mid ← (left + right) // 2
        if A[mid] == target:
            return mid
        else if A[mid] < target:
            left ← mid + 1
        else:
            right ← mid - 1
    return -1
"""

**Issue**: The array `A` may contain **duplicate values**, and you want to find the **first occurrence** of the target value.

### Task:
- Modify the pseudocode to ensure it **returns the first index** of the target if duplicates exist.
- Explain what you changed and why it works.
- Discuss how the time complexity is affected, if at all.