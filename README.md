    Group Members:

    LYDIA YOSEPH             UGR/7809/15

    MESERET GHEBIRESILASSIE  UGR/0722/15

    MIKIYAS FASIL            UGR/9231/15

    SALEM GEBRU              UGR/6916/15

    Section - 2

Branch and Bound Algorithm – 0/1 Knapsack Problem

Project Description

This repository contains a Python implementation of the Branch and Bound algorithm applied to the 0/1 Knapsack problem. The implementation demonstrates how combinatorial optimization problems can be solved optimally by systematically exploring a state space tree while pruning suboptimal branches using bounding techniques. This project was developed as part of an Introduction to Artificial Intelligence course assignment and focuses on illustrating both the theoretical foundations and the practical behavior of the Branch and Bound method.

Problem Statement

The 0/1 Knapsack problem aims to select a subset of items, each with an associated weight and value, such that the total weight of the selected items does not exceed the knapsack capacity while the total value is maximized. Each item can either be included or excluded, and fractional selection of items is not allowed. This problem is NP-hard and is commonly used to demonstrate exact optimization techniques such as the Branch and Bound algorithm.

Algorithm Overview

The Branch and Bound algorithm explores the solution space using a state space tree. At each node in the tree, the algorithm makes a binary decision to either include or exclude the current item, which results in branching. For each node, an upper bound on the maximum achievable profit is computed using a fractional knapsack relaxation, which allows partial inclusion of items for estimation purposes only. Pruning occurs when the bound of a node is not greater than the current best profit, also known as the incumbent, since such a node cannot lead to a better solution. The algorithm uses a Breadth-First Search strategy implemented with a queue to traverse the state space tree. This approach guarantees an optimal solution while avoiding exhaustive enumeration of all possible combinations.

Implementation Details

The implementation uses only standard Python libraries. An Item class is used to represent knapsack items with weight and value attributes. A Node class represents a state in the search tree and stores the current level, the total profit accumulated so far, the total weight accumulated so far, and an upper bound estimate of the achievable profit from that node. Before the search begins, items are sorted in decreasing order of their value-to-weight ratio to improve the effectiveness of the bounding function. The bounding function uses a greedy fractional knapsack approach to compute an optimistic profit estimate. Python’s queue.Queue is used to implement Breadth-First Search traversal of the state space tree, and the algorithm terminates when the queue becomes empty.

How to Run the Code

The program requires Python version 3.x. To run the code, execute the following command in the terminal: python knapsack_bnb.py. The example input is defined directly in the code, where the knapsack capacity is set to 10 and the list of items is specified with their respective weights and values.

Sample Output

When executed with the example input, the program outputs the maximum possible profit that can be achieved without exceeding the knapsack capacity. The actual output depends on the input items and the specified capacity.

Limitations

The Branch and Bound algorithm has exponential worst-case time complexity, especially when the bounding function is weak. The use of Breadth-First Search may lead to high memory usage due to the storage of multiple active nodes in the queue. Additionally, the performance of the algorithm is highly dependent on the quality of the bounding function. This implementation also does not track which specific items are selected in the optimal solution and only returns the maximum achievable profit.

Possible Improvements

The performance of the algorithm can be improved by using a priority queue to implement Best-First Search, allowing more promising nodes to be explored earlier. Switching to Depth-First Search can reduce memory usage in cases where memory is a constraint. The implementation can also be extended to track and return the selected items that form the optimal solution. Parallel processing may be introduced to explore independent branches of the search tree concurrently, and more problem-specific heuristics can be developed to strengthen the bounding function.
