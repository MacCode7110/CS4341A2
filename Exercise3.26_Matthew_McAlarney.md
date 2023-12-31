# Chapter 3 Exercise 3.26

Consider the unbounded version of the regular 2D grid shown in Figure 3.9. The start
state is at the origin, (0,0), and the goal state is at (x, y).

    a. What is the branching factor b in this state space?

        The branching factor b in the state space is 4. This is because at node (0,0) in the initial state, there are 4 possible states to transition to (4 other nodes that can be reached in other words).

    b. How many distinct states are there at depth k (for k > 0)? 

        At depth 1, we know that there are 4 distinct states (the current frontier at depth 1) because 4 new nodes have been expanded from the root node as shown in phase a.
        At depth 2, we know that there are 8 distinct states (the current frontier ar depth 2) because 8 new nodes have been expanded from the 4 distinct states as shown in phase c.
        At depth k for k > 0, there are (4 * k) distinct states.

    c. What is the maximum number of nodes expanded by breadth-first tree search? 

        Breadth-first search expands all successors of the current node.
        For a tree search, we can visit the same node multiple times. Tree search does not care about repeating nodes. A given node cannot be expanded multiple times but it can repeat in the tree and therefore be visited multiple times. Final maximum should be an exponential result.
        According to the textbook, the time complexity of breadth-first search for a solution at depth d with branching factor b is O(b^d). The depth of a solution at coordinate (x, y) can be calculated as d = x + y. 
        Therefore, the maximum number of nodes expanded by breadth-first tree search for a solution at depth d is 4^((x + y) - 1), and the -1 accounts for the fact that leaf nodes on the frontier would not be expanded yet.

    d. What is the maximum number of nodes expanded by breadth-first graph search? 

        For a graph search, we cannot visit the same node multiple times. There are no repeated paths. Final maximum should be a quadratic result.
        The maximum number of nodes expanded is cumulative through the graph depths.
        For a solution at depth 1, there is a maximum of 1 node that has been expanded (the root node).
        For a solution at depth 2, there is a maximum of 5 nodes that have been expanded including the root node (the number of nodes expanded is cumulative). 
        For a solution at depth 3, there would be a maximum of 13 nodes that have been expanded including the 5 nodes that have been expanded for depth 2.
        For a solution at depth d, the maximum number of nodes expanded by breadth-first graph search takes the form of a quadratic equation:
        2(d^2) - 2d + 1 where d = x + y for a goal state at coordinate (x, y) as mentioned in part c. The + 1 at the end accounts for the expansion of the root node.

    e. Is h = |u − x| + |v − y| an admissible heuristic for a state at (u, v)? Explain.

        Heuristic function h(n) = estimated cost of the cheapest path from the state at node n to a goal state.
        We know that a heuristic function is admissible if it never overestimates the cost to reach a goal for every node n.

        Yes, h = |u - x| + |v - y| is an admissible heuristic function. This is because the heuristic function calculates the cheapest grid distance between a state at (u, v) and the goal state. This heuristic will never overestimate the distance between these two states for each node because the only directions that can be used to move through the grid are up, down, left, and right. For exmaple, it is impossible to move diagonally from initial (0,0) to goal state (1,1). The heuristic function calculates the cheapest path, which in this case is 2. 

    f. How many nodes are expanded by A∗ graph search using h?

        When using A* graph search using heuristic h, we are really computing a best-first search using evaluation function f(n) = g(n) + h(n) where g(n) is the path cost from the initial state to node n and h(n) is the heuristic function passed as a parameter.
        Therefore, we know that x + y nodes are expanded using A* graph search with heuristic h. x + y is always equal to the length of the cheapest/shortest path from the initial state to the goal state.

    g. Does h remain admissible if some links are removed?

        If some links on the grid are removed, h does indeed remain admissible. Since the basic four directions of exploring the grid (up, down, left, right) are still present, h will still estimate the cost of the cheapest path from the state at node n to a goal state, which also means that in certain cases, h(n) will underestimate the cost of the cheapest path, which is perfectly fine.
        Even if h(n) underestimates the cost of the cheapest path, it still remains admissible as it still will never overestimate the cost to reach the goal state.

    h. Does h remain admissible if some links are added between nonadjacent states?

        h does not remain admissible if some links are added between nonadjacent states. 
        Reasoning: If some links are added between nonadjacent states, then this means that some states will be connected through diagonal links (as all adjacent states are connected through either vertical or horizontal links). If the initial state is (0,0) and the goal state is (1,1) for instance, then h will still produce a path length estimate of 2 while the cheapest path length is actually 1. Thus, there is at least one case where the heuristic h overestimates the cost to reach a goal state from the initial state, which means that h cannot be admissible.