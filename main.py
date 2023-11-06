# Chapter 4 Exercise 4.3

# In this exercise, we explore the use of local search methods to solve TSPs of the type defined in Exercise 3.30.

# -----

# Exercise 3.30 Description:

# The traveling salesperson problem (TSP) can be solved with the minimum-spanning tree (MST) heuristic,
# which estimates the cost of completing a tour, given that a partial tour
# has already been constructed. The MST cost of a set of cities is the smallest sum of the link
# costs of any tree that connects all the cities.

# -----

# a. Implement and test a hill-climbing method to solve TSPs.
# b. Repeat part (a) using a genetic algorithm instead of hill climbing.
# You may want to consult Larra˜naga et al. (1999) for some suggestions for representations.

# -----

# Part a - Hill-climbing algorithm implementation to solve TSPs:

class HillClimbing:

    def __init__(self, tsp_problem, initial_starting_node):
        self.tsp_problem = tsp_problem
        self.initial_starting_node = initial_starting_node

    def run_hill_climbing_algorithm(self):
        self


# A GraphSegment class that creates an object that puts together the following information:
# a starting node, ending node, and the distance from the starting node to the ending node.
class GraphSegment:

    def __init__(self, starting_node, ending_node, distance):
        self.starting_node = starting_node
        self.ending_node = ending_node
        self.distance = distance


# Part b - Genetic algorithm implementation to solve TSPs:


# Test data used to test both the hill-climbing and genetic algorithm implementations:

# part a test data:
traveling_sales_person_graph_1 = {
    'A': [GraphSegment('A', 'B', 40), GraphSegment('A', 'C', 60), GraphSegment('A', 'D', 10)],
    'B': [GraphSegment('B', 'A', 40), GraphSegment('B', 'C', 50), GraphSegment('B', 'D', 20)],
    'C': [GraphSegment('C', 'A', 60), GraphSegment('C', 'B', 50), GraphSegment('C', 'D', 30)],
    'D': [GraphSegment('D', 'A', 10), GraphSegment('D', 'B', 20), GraphSegment('D', 'C', 30)]
}

hill_climbing_test_1 = HillClimbing(traveling_sales_person_graph_1, 'A')
hill_climbing_test_1.run_hill_climbing_algorithm()

# part b test data:
