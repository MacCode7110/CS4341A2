# Chapter 3 Exercise 3.3

3.3 Suppose two friends live in different cities on a map, such as the Romania map shown
in Figure 3.2. On every turn, we can simultaneously move each friend to a neighboring city on
the map. The amount of time needed to move from city i to neighbor j is equal to the road
distance d(i, j) between the cities, but on each turn the friend that arrives first must wait until
the other one arrives (and calls the first on his/her cell phone) before the next turn can begin.
We want the two friends to meet as quickly as possible.
    
    a. Write a detailed formulation for this search problem. (You will find it helpful to define
    some formal notation here.)

    Assumptions:
        1. If the two friends meet at different cities at the same time, then there is no need for one friend to wait for the other.
        2. In our formal notation, we will denote the city that one friend currently occupies as c1, and the city the other friend currently occupies as c2.

    State Space: 
        All possible pairs of cities where there is at least one city that both friends can occupy at the same time, which is represented as (c1, c2).
    
    Initial State: 
        Any pair of cities where one friend occupies a city in the pair and the other friend occupies a city in the pair.
    
    Goal States: 
        Any pair of cities occupied by both friends in the state space (c1, c2) where c1 = c2. That is, both friends have reached each other through arriving at the same city.
    
    Actions: 

        List of actions:
            Each friend can do the following:
                1. Move from city i to neighboring city j.
        
        Notation to represent the list of actions above:
            
            Based on the textbook, we know the following: "Given a state s, Actions(s) returns a finite set of actions that can be executed in s."
            
            Notation: Actions((c1, c2)) = (A1, A2) where (A1, A2) is the set of actions that can be executed in state (c1, c2).
            
            A1 is the subset of actions that can be executed in c1 and A2 is the subset of actions that can be executed in c2.

    Transitional Model:
        
        According to the textbook, we know that Result(s, a) returns the state that results from doing action a in state s. 
        
        Notation to represent the transitional model: 
            
            Let a1 be a single action from subset A1
            Let a2 be a single action from subset A2

            Result((c1, c2), (a1, a2)) = (c1', c2') where (c1', c2') is the state that results from executing action a1 in c1 (in state (c1, c2) overall) and executing action a2 in c2 (in state (c1, c2) overall).

    Action-Cost Function:
    
        According to the textbook, we know that "an action cost function, denoted by Action-Cost(s, a, s') when we are programming or c(s, a, s')
        when we are doing math, that gives the numeric cost of applying action a in state s to reach state s'."

        Notation to represent the action-cost function:

            Let a1 be a single action from subset A1
            Let a2 be a single action from subset A2
            Let the cost of the action of moving from city i to neighboring city j be the amount of time it takes to move between the cities defined as d(i, j).

            Action-Cost((c1, c2), (a1, a2), (c1', c2')) = d(c1, c1') + d(c2, c2')

            Explanation: On each turn, the total cost of the actions of both friends is the sum of the amount of time it takes for each of them to travel from c1 to c1' and from c2 to c2' respectively. Both definitions d(c1, c1') and d(c2, c2') account for the potential time that one friend will wait on the other friend to arrive at a city.

    b. Let D(i, j) be the straight-line distance between cities i and j. Which of the following
    heuristic functions are admissible? (i) D(i, j); (ii) 2 · D(i, j); (iii) D(i, j)/2.

        Heuristic function h(n) = estimated cost of the cheapest path from the state at node n to a goal state.
        We know that a heuristic function is admissible if it never overestimates the cost to reach a goal.

        (i) D(i, j) is an admissible heuristic because D(i, j) is the straight-line distance between cities i and j, which also makes it the cheapest path between the two cities. Using D(i, j) as a heuristic function will never overestimate the time it takes to move from city i to city j as it is the cheapest path, which also makes this heuristic function admissible.

    c. Are there completely connected maps for which no solution exists?

        Under the assumptions listed in the problem formulation, a connected map containing only two cities does not have a solution. Both friends must move from one city to another until they meet each other in the same city. In a connected map containing only two cities, two friends will never be able to meet each other in the same city as one friend will always arrive in one of the cities and the other friend will always arrive in the other city.

    d. Are there maps in which all solutions require one friend to visit the same city twice?

        Yes, there are maps in which all solutions require one friend to visit the same city twice. These maps involve one friend needing to follow a loop back to their starting city before meeting the other friend at the same city.

        Here is an example map:

        Friend 1 begins at city X
        Friend 2 begins at city Y
        Cities are denoted by an uppercase alphabetical letter.

        H - J - X - Q - I - E - N - M - Y
        |       |
        L - V - S

        In the map above, friends 1 and 2 must each make 6 moves between cities before meeting at city X. In order for both friends to meet at city X, Friend 1 must follow a loop back to this city, which means that Friend 1 will have visited City X twice. 