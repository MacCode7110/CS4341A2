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
            2. Curved pieces and fork pieces can be flipped over to curve in either direction.
            3. Two railway pieces form a connection when the socket of one piece locks with the peg of another piece.
            4. There is a total of 32 pieces in the set of railway pieces. The set of railway pieces is made up of the following distinct tracks as shown in Figure 3.32:
                a. Straight pieces (quantity of 12)
                b. Curved pieces (quantity of 16)
                c. Fork pieces with 2 pegs (quantity of 2)
                d. Fork pieces with 1 peg (quantity of 2)

        State Space: 
            Two pieces of information make up the state space:
                1. The first railway piece to be plotted on the floor, which is chosen trivially from the set.
                2. The number of connected railway pieces.
    
        Initial State: 
            The first railway piece to be plotted on the floor, which is chosen trivially from the set.
    
        Goal States: 
            32 railway pieces are connected and form a railway without any overlapping tracks or loose ends.

        Actions: 

            1. Connect Railway Piece: A railway piece picked out of the subset of unconnected railway pieces can be connected to an open socket or peg of the piece that was previously connected to the railway.
            2. Remove Railway Piece: 
                a. If there are no railway pieces in the subset of unconnected pieces that can connect to the open socket or peg of the piece that was previously connected to the railway, then this piece that was previously connected to the railway will be removed and placed back in the subset of unconnected railway pieces.
                b. If there are no railway pieces in the subset of unconnected pieces that can connect to the open socket or peg of the piece that was previously connected to the railway without overlapping another railway piece, then the piece that was previously connected to the railway will be removed and placed back in the subset of unconnected railway pieces.
        
        Transitional Model:
        
            1. Each time that a railway piece is connected to the railway through the Connect Railway Piece action, the number of connected railway pieces increments by 1, which results in a change in state.
            2. Each time that a railway piece is removed from the railway through the Remove Railway Piece action, the number of connected railway pieces decrements by 1, which results in a change in state.

        Action-Cost Function:
    
            Since the goal state is to have 32 railway pieces connected that form a railway without any overlapping tracks or loose ends, the action of removing a railway piece from the railway delays achieving the goal state.
            Therefore, for each railway piece that is removed from the railway, the numeric cost increments by 1.

    b. Identify a suitable uninformed search algorithm for this task and explain your choice.

        A suitable uninformed search algorithm for this task is depth-first search. The task of building a connected railway involves a finite state space. Thus, there is no need to keep track of a table of reached nodes in the railway building problem and the depth-first search algorithm does not require keeping a table of reached nodes either.
        The railway problem structure and depth-first search have smaller memory demands than breadth-first search as a result of not needing to keep track of a table of reached nodes; breadth-first search would not be the ideal algorithm choice for this problem.
        In addition, with depth-first search, the frontier is also relatively small. In the case of the railway problem, depth-first search is a good fit because the frontier only involves the deepest node that is unexpanded, which would be the railway piece most recently connected. 
        Furthermore, it is already known that all solutions to the railway problem occur on the same level of depth (32 nodes deep), which makes depth-first search a more efficient search algorithm for finding one of these solutions than a breadth-first search, which would instead search for a wider range of paths earlier on in the railway. 

    c. Explain why removing any one of the “fork” pieces makes the problem unsolvable.

        Removing any one of the "fork" (switch) pieces makes the problem unsolvable because this would result in an incorrect number of branches preventing the construction of a complete railway. 
        When the incorrect number of fork pieces and branches are present, the railway is guaranteed to contain at least one loose end, which would make it impossible for a search algorithm to find a solution (path to the goal state).

    d. Give an upper bound on the total size of the state space defined by your formulation.
    (Hint: think about the maximum branching factor for the construction process and the
    maximum depth, ignoring the problem of overlapping pieces and loose ends. Begin by
    pretending that every piece is unique.) **

        Upper bound on the total size of the state space:
        
            We have 32 pieces total and after the first piece is plotted, we have 31 pieces remaining to plot.
            There are 20 pieces total that can be rotated in two different directions (16 X curved pieces, 2 X fork pieces with one peg, 2 X fork pieces with two pegs)
            The upper bound on the total size of the state space can be written as follows: 31! * (12 + (16 * 2) + (2 * 2) + (2 * 2))