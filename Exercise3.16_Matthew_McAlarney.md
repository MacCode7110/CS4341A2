# Chapter 3 Exercise 3.16

A basic wooden railway set contains the pieces shown in Figure 3.32. The task is to
connect these pieces into a railway that has no overlapping tracks and no loose ends where a
train could run off onto the floor.

    Example railway with no overlapping tracks and loose ends (forms a loop):

    / - - - \
    |       |
    |       |
    \ - - - /

    a. Suppose that the pieces fit together exactly with no slack. Give a precise formulation of
    the task as a search problem.

        Assumptions:
            1. In order for the railway to have no overlapping tracks and loose ends where a train could run off onto the floor, all railway tracks must be connected to each other.
            2. The railway system takes the form of a graph and each railway piece is a node. The connections between railway pieces are edges.
            3. Curved pieces and fork pieces can be flipped over to curve in either direction.
            4. Two railway pieces form a connection when the socket of one piece locks with the peg of another piece.
            5. There is a total of 32 pieces in the set of railway pieces. The set of railway pieces is made up of the following distinct tracks as shown in Figure 3.32:
                a. Straight pieces (quantity of 12)
                b. Curved pieces (quantity of 16)
                c. Fork pieces with 2 pegs (quantity of 2)
                d. Fork pieces with 1 peg (quantity of 2)

        State Space: 
            Three pieces of information make up the state space:
                1. The first railway piece to be plotted on the floor, which is chosen trivially from the set.
                2. The number of connected railway pieces.
                3. A pointer to the most recently connected railway piece.
    
        Initial State: 
            The first railway piece to be plotted on the floor, which is chosen trivially from the set.
    
        Goal States: 
            32 railway pieces are connected and form a railway without any overlapping tracks or loose ends.

        Actions: 

            1. Connect Railway Piece: A railway piece picked out of the subset of unconnected railway pieces can be connected to an open socket or peg of a piece that was previously connected to the railway. The previously connected piece that is selected in the following priority is (1) if a loop was just connected together, a connected fork piece with at least one remaining open peg or socket or (2) else, the piece that was most recently connected to the railway. 
            2. Remove Railway Piece: 
                a. If there are no railway pieces in the subset of unconnected pieces that can connect to the open socket or peg of a piece that was previously connected to the railway, then the selected piece that was previosuly connected to the railway will be removed and placed back in the subset of unconnected railway pieces. The previously connected piece that is selected in the following priority is (1) if a loop was just connected together, a connected fork piece with at least one remaining open peg or socket or (2) else, the piece that was most recently connected to the railway.
                b. If there are no railway pieces in the subset of unconnected pieces that can connect to the open socket or peg of a piece that was previously connected to the railway without overlapping another railway piece, then the selected piece that was previously connected to the railway will be removed and placed back in the subset of unconnected railway pieces. The previously connected piece that is selected in the following priority is (1) if a loop was just connected together, a connected fork piece with at least one remaining open peg or socket or (2) else, the piece that was most recently connected to the railway.
        
        Transitional Model:
        
            1. Each time that a railway piece is connected to the railway through the Connect Railway Piece action, the number of connected railway pieces increments by 1, which results in a change in state.
            2. Each time that a railway piece is removed from the railway through the Remove Railway Piece action, the number of connected railway pieces decrements by 1, which results in a change in state.

        Action-Cost Function:
    
            Since the goal state is to have 32 railway pieces connected that form a railway without any overlapping tracks or loose ends, the action of removing a railway piece from the railway delays achieving the goal state.
            Therefore, for each railway piece that is removed from the railway, the numeric cost increments by 1.

    b. Identify a suitable uninformed search algorithm for this task and explain your choice.

        A suitable uninformed search algorithm for this task is depth-first search. 
        (1) The state space for the railway building problem takes the form of a graph structure where loops are needed to prevent loose ends from occurring. Fork and curve pieces allow for the construction of loops in the railway to form a graph structure. Loop formations are allowed in graph structures.
        (2) The task of building a connected railway not only takes the form of a graph structure, but also involves a finite state space. These two pieces of information form a problem that fits depth-first search as this algorithm does perform well on finite graph-shaped state spaces. There is no need to keep track of a table of reached nodes in the railway building problem and the depth-first search algorithm does not require keeping a table of reached nodes either.
        (3) The railway problem structure and depth-first search have smaller memory demands than breadth-first search as a result of not needing to keep track of a table of reached nodes; breadth-first search would not be the ideal algorithm choice for this problem.
        (4) In addition, with depth-first search, the frontier is also relatively small. In the case of the railway problem, depth-first search is a good fit because the frontier only involves the deepest node that is unexpanded, which would be the railway piece most recently connected. 
        (5) Furthermore, it is already known that all solutions to the railway problem occur only when 32 railway pieces are connected, which makes depth-first search a more efficient search algorithm (faster and fewer number of actions taken) for finding one of these solutions than a breadth-first search, which would instead unnecessarily search for a wider range of paths earlier on in the railway system. 
        
    c. Explain why removing any one of the “fork” pieces makes the problem unsolvable.

        Removing any one of the "fork" (switch) pieces makes the problem unsolvable because this would result in an incorrect number of railway branches, which would prevent the construction of a complete railway. 
        When the incorrect number of fork pieces and railway branches are present, the railway is guaranteed to contain at least one loose end, which would make it impossible for a search algorithm to find a solution (path to the goal state).

    d. Give an upper bound on the total size of the state space defined by your formulation.
    (Hint: think about the maximum branching factor for the construction process and the
    maximum depth, ignoring the problem of overlapping pieces and loose ends. Begin by
    pretending that every piece is unique.) 

        Upper bound on the total size of the state space:
        
            We have 32 pieces total to plot, and there are 20 pieces total that can be rotated in two different directions (16 X curved pieces, 2 X fork pieces with one peg, 2 X fork pieces with two pegs). There are also 12 straight railway pieces.
            The upper bound on the total size of the state space accounting for the two different directions that 20 pieces can be rotated towards takes the form of a permutation, which can be written as follows: 32! * (12 + (16 * 2) + (2 * 2) + (2 * 2))