## 🧠 Open Question 1 – Recursion (10 points)

**Problem: Count Zeros in a Number**

Write a **recursive function** that counts how many times the digit `0` appears in a non-negative integer `n`.

### Example:
Input: `n = 2040`  
Output: `2`

### Requirements:
- Use recursion (no string conversion).
- Clearly define base case and recursive case.
- Analyze time complexity in terms of the number of digits.

---

## 🌳 Open Question 2 – Binary Tree Tasks (15 points)

You are given this binary tree represented as a list:  
`[5, 3, 8, 1, 4, 7, 9]`  
(Assume the list represents level-order traversal and it is a valid binary search tree.)

### Tasks:
1. Draw the binary tree.
2. Write a recursive function to compute the **sum of all nodes at level `k`**, where `k` is a given integer (root is at level 0).
3. Write a function to check if the tree is **height-balanced** (difference in height of subtrees ≤ 1 at every node).
4. Is this tree complete? Is it perfect? Explain your answers.

---

## 🔗 Open Question 3 – Graph Problem (15 points)

You are given a graph of course prerequisites:

```
Courses: CS101, CS102, CS103, CS104  
Prerequisites:
- CS102 depends on CS101
- CS103 depends on CS101
- CS104 depends on CS102 and CS103
```

### Tasks:
1. Model the graph using an adjacency list.
2. Perform topological sort and list a valid course order.
3. Write pseudocode for detecting **cycles** in a directed graph using DFS.
4. Explain what the presence of a cycle would mean in the context of course scheduling.

---

## 🔧 Open Question 4 – Pseudocode Modification (10 points)

You are given pseudocode that performs linear search on an array:

"""
function LinearSearch(A, target):
    for i from 0 to length(A) - 1:
        if A[i] == target:
            return i
    return -1
"""

### Tasks:
1. Modify the function so that it **returns all indices** where the target occurs, not just the first one.
2. Return a list of positions instead of a single index.
3. Does the time complexity change? Justify your answer.