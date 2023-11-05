# Chapter 4 Exercise 4.2

Exercise 3.16 considers the problem of building railway tracks under the assumption
that pieces fit exactly with no slack. Now consider the real problem, in which pieces don’t
fit exactly but allow for up to 10 degrees of rotation to either side of the “proper” alignment.
Explain how to formulate the problem so that it could be solved by simulated annealing.

    New Problem Formulation:

    Updated Assumptions:
        1. In order for the railway to have no overlapping tracks and loose ends where a train could run off onto the floor, all railway tracks must be connected to each other.
        2. Curved pieces and fork pieces can be flipped over to curve in either direction.
        3. Two railway pieces form a connection when the socket of one piece locks with the peg of another piece.
        4. The greater the degree of rotation of a railway piece, the further away it is from the proper alignment.
        5. There is a total of 32 pieces in the set of railway pieces. The set of railway pieces is made up of the following distinct tracks as shown in Figure 3.32:
            a. Straight pieces (quantity of 12)
            b. Curved pieces (quantity of 16)
            c. Fork pieces with 2 pegs (quantity of 2)
            d. Fork pieces with 1 peg (quantity of 2)

    Updated State Space: 
        Since pieces can rotate up to 10 degrees to either side of the proper alignment, we know that the state space is continuous as there is an infinite number of angles up to 10 degrees.
        Since the state space is continuous, each state now holds the following information:
            1. The first railway piece to be plotted on the floor, which is chosen trivially from the set.
            2. The number of connected railway pieces.
            3. The degree of rotation for each connected piece.
    
    Initial State: 
        The first railway piece to be plotted on the floor, which is chosen trivially from the set.
    
    Updated Goal States: 
        Let E be an evaluation function applied as a goal test to each state.
        In this real world version of the railway problem, the best possible goal state is the state where all 32 railway pieces are connected and the degrees of rotation for each piece add together to the smallest possible sum.
        The best possible state involves finding the smallest sum of degrees of rotation for the 32 connected pieces; ideally, we would like all of the railway pieces to fit together as close to their proper alignments as possible. 
        In evaluation function E, the following statuses of the railway are checked to determine if a goal state has been found:
            1. 32 railway pieces are connected and form a railway without any overlapping tracks or loose ends.
            2. If the degrees of rotation for the 32 connected pieces sum to the smallest possible value, then the agent has found the best possible goal state.

    Updated Actions: 

        1. Connect Railway Piece (railway_piece, degree_of_rotation): A railway piece picked out of the subset of unconnected railway pieces can be connected to an open socket or peg of the piece that was previously connected to the railway. The new piece to be connected (passed to the railway_piece parameter) also has a degree_of_rotation parameter, which specifies the degree of rotation from the proper alignment when performing the connection.
        2. Adjust Degree of Rotation (connected_railway_piece, new_degree_of_rotation): The degree of rotation of any connected railway piece (specified in the connected_railway_piece parameter) can be adjusted to the angle specified in the new_degree_of_rotation parameter. The new_degree_of_rotation argument is valid only if it meets the following requirements: (1) specifies an angle that is no greater than 10 degrees of rotation to either side of the proper alignment. (2) specifies an angle such that the railway piece still maintains connections with neighboring railway pieces.
        3. Remove Railway Piece: 
            a. If there are no railway pieces in the subset of unconnected pieces that can connect to the open socket or peg of the piece that was previously connected to the railway, then this piece that was previously connected to the railway will be removed and placed back in the subset of unconnected railway pieces.
            b. If there are no railway pieces in the subset of unconnected pieces that can connect to the open socket or peg of the piece that was previously connected to the railway without overlapping another railway piece, then the piece that was previously connected to the railway will be removed and placed back in the subset of unconnected railway pieces.
        
    Updated Transitional Model:
        
        1. Each time that a railway piece is connected to the railway through the Connect Railway Piece action, the number of connected railway pieces increments by 1. In addition, the degree of rotation for the newly connected piece is accounted for in the state space. Both of these pieces of information result in a change in state.
        2. Each time the degree of rotation of a railway piece is adjusted, a new degree of rotation for the specified piece is accounted for in the state space, which results in a change in state.
        3. Each time that a railway piece is removed from the railway through the Remove Railway Piece action, the number of connected railway pieces decrements by 1, which results in a change in state.

    Updated Action-Cost Function:
    
        Since the goal state is to have 32 railway pieces connected that form a railway without any overlapping tracks or loose ends, the action of removing a railway piece from the railway delays achieving the goal state.
        In addition, needing to adjust the angles of railway pieces to obtain a goal state or potentially the best possible goal state also causes a delay.
        For each railway piece that is removed from the railway, the numeric cost increments by 1.
        For each degree of rotation that is adjusted, the numeric cost increments by 1.5.

    How the new problem could be solved using simulated annealing:

        *How to think about this?*