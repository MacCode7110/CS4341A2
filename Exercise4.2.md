# Chapter 4 Exercise 4.2

Exercise 3.16 considers the problem of building railway tracks under the assumption
that pieces fit exactly with no slack. Now consider the real problem, in which pieces don’t
fit exactly but allow for up to 10 degrees of rotation to either side of the “proper” alignment.
Explain how to formulate the problem so that it could be solved by simulated annealing.

    New Problem Formulation:

    Updated Assumptions:
        1. In order for the railway to have no overlapping tracks and loose ends where a train could run off onto the floor, all railway tracks must be connected to each other.
        2. The railway system takes the form of a graph and each railway piece is a node. The connections between railway pieces are edges.
        3. Curved pieces and fork pieces can be flipped over to curve in either direction.
        4. Two railway pieces form a connection when the socket of one piece locks with the peg of another piece.
        5. The greater the degree of rotation of a railway piece, the further away it is from the proper alignment.
        6. There is a total of 32 pieces in the set of railway pieces. The set of railway pieces is made up of the following distinct tracks as shown in Figure 3.32:
            a. Straight pieces (quantity of 12)
            b. Curved pieces (quantity of 16)
            c. Fork pieces with 2 pegs (quantity of 2)
            d. Fork pieces with 1 peg (quantity of 2)

    Updated State Space: 
        Since pieces can rotate up to 10 degrees to either side of the proper alignment, we know that the state space is continuous as there is an infinite number of angles up to 10 degrees.
        Since the state space is continuous, each state now holds the following information:
            1. The first railway piece to be plotted on the floor, which is chosen trivially from the set.
            2. The number of connected railway pieces.
            3. A pointer for each connected railway piece and the degree of rotation for each connected piece.
    
    Initial State: 
        The first railway piece to be plotted on the floor, which is chosen trivially from the set.
    
    Updated Goal States: 
        Let E be an evaluation function applied as a goal test to each state.
        In this real world version of the railway problem, the best possible goal state is the state where all 32 railway pieces are connected and the degrees of rotation for each piece add together to the smallest possible sum.
        The best possible state involves finding the smallest sum of degrees of rotation for the 32 connected pieces; ideally, we would like all of the railway pieces to fit together as close to their proper alignments as possible. 
        In evaluation function E, the following statuses of the railway are checked to determine if a goal state has been found:
            1. 32 railway pieces are connected and form a railway without any overlapping tracks or loose ends.
            2. If the degrees of rotation for the 32 connected pieces sum to the smallest possible value, then the agent has found the best possible goal state/solution.

    Updated Actions: 

        1. Connect Railway Piece (railway_piece, degree_of_rotation): A railway piece picked out of the subset of unconnected railway pieces can be connected to an open socket or peg of a piece that was previously connected to the railway. The previously connected piece that is selected in the following priority is (1) if a loop was just connected together, a connected fork piece with at least one remaining open peg or socket or (2) else, the piece that was most recently connected to the railway. The new piece to be connected (passed to the railway_piece parameter) also has a degree_of_rotation parameter, which specifies the degree of rotation from the proper alignment when performing the connection.
        2. Adjust Degree of Rotation (connected_railway_piece, new_degree_of_rotation): The degree of rotation of any connected railway piece (specified in the connected_railway_piece parameter) can be adjusted to the angle specified in the new_degree_of_rotation parameter. The new_degree_of_rotation argument is valid only if it meets the following requirements: (1) specifies an angle that is no greater than 10 degrees of rotation to either side of the proper alignment. (2) specifies an angle such that the railway piece still maintains connections with neighboring railway pieces.
        3. Remove Railway Piece: 
            a. If there are no railway pieces in the subset of unconnected pieces that can connect to the open socket or peg of a piece that was previously connected to the railway, then the selected piece that was previously connected to the railway will be removed and placed back in the subset of unconnected railway pieces. The previously connected piece that is selected in the following priority is (1) if a loop was just connected together, a connected fork piece with at least one remaining open peg or socket or (2) else, the piece that was most recently connected to the railway.
            b. If there are no railway pieces in the subset of unconnected pieces that can connect to the open socket or peg of a piece that was previously connected to the railway without overlapping another railway piece, then the selected piece that was previously connected to the railway will be removed and placed back in the subset of unconnected railway pieces. The previously connected piece that is selected in the following priority is (1) if a loop was just connected together, a connected fork piece with at least one remaining open peg or socket or (2) else, the piece that was most recently connected to the railway.
        
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

        Simulated annealing is used to solve optimization problems and is designed to find the best possible solution.
        With the introduction of degrees of rotation for all pieces, this version of the railway building problem is now an optimization problem because there is now a best possible solution that can be achieved.
        The best possible solution in this version of the railway building problem is the goal state where the degrees of rotation of the 32 connected pieces sums to the smallest possible value. This smallest possible sum of the degrees of rotation of all connected railway pieces is the global minimum that a simulated annealing algorithm can find.
        Simulated annealing is capable of solving the new railway building problem, and it also works because the updated state space is now continuous; the continuous state space allows for small adjustments to be made to the degrees of rotation for each railway piece. These small adjustments makes it more likely that simulated annealing avoids the issue of getting stuck in local minima.
        
        Algorithmic steps that simulated annealing can use to find the best possible solution to the railway building problem:
            1. Plot the first railway piece picked trivially from the subset of unconnected railway pieces on the floor (this creates the initial state). This action is always accepted regardless of the chosen starting piece as it brings the agent closer to a goal state.
            2. Pick a move at random:
                a. The action of connecting a railway piece is accepted as long as the specified piece can be connected to the selected previously connected railway piece. The connect railway piece action also brings the agent closer to a goal state (a way of improving the current situation).
                b. The action of removing a connected railway piece is only accepted if (1) no railway pieces from the subset of unconnected pieces can be connected to the selected previously connected piece OR (2) no railway pieces from the subset of unconnected pieces can be connected to the selected previously connected piece without causing an overlap with another piece.
                c. The action of adjusting the degree of rotation of any connected railway piece:
                    I. Is always accepted if the specified degree of rotation is smaller than the current degree of rotation of the selected piece and is smaller than the degree of rotation of the most recently connected piece. A state space of connected pieces with continually smaller degrees of rotation always takes steps towards minimizing the sum of all degrees of rotation, which brings the agent closer to the best possible goal state/solution (improves the current situation).
                    II. Is accepted with a probability less than 1 (likely between 0.5 and 0.99) if the specified degree of rotation is greater than or equal to the current degree of rotation of the selected piece and is still smaller than or equal to the degree of rotation of the most recently connected piece. This move is objectively worse than the one in item I as it will never bring the agent closer to the best possible solution, and so it is accepted with a probability less than 1.
                    III. Is accepted with a probability less than 1 (likely between 0.01 and 0.49) if the specified degree of rotation is greater than the current degree of rotation of the selected piece and is greater than the degree of rotation of the most recently connected piece. This move is objectively the worst one compared to items I and II as it pushes the agent further away from the best possible solution, and so it is accepted with a probability that is less than 1 and less than the range of probabilities listed in item II.
