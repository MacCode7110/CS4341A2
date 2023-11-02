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
        3. Both friends can occupy the same city simultaneously.

    State Space: 
        All possible pairs of cities where there is at least one city that both friends can occupy at the same time, which is represented as (c1, c2).
    
    Initial State: 
        Any pair of cities where one friend occupies a city in the pair and the other friend occupies a city in the pair.
    
    Goal States: 
        Any pair of cities occupied by both friends in the state space (c1, c2) where c1 = c2. That is, both friends occupy the same city at the same time (they have finally met each other in the same city).
    
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



    c. Are there completely connected maps for which no solution exists?



    d. Are there maps in which all solutions require one friend to visit the same city twice?

