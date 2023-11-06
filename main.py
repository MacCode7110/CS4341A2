# Chapter 4 Exercise 4.3

# In this exercise, we explore the use of local search methods to solve TSPs of the type defined in Exercise 3.30.

# Exercise 3.30 Description:

# The traveling salesperson problem (TSP) can be solved with the minimum-spanning tree (MST) heuristic,
# which estimates the cost of completing a tour, given that a partial tour
# has already been constructed. The MST cost of a set of cities is the smallest sum of the link
# costs of any tree that connects all the cities.

# a. Implement and test a hill-climbing method to solve TSPs.
# b. Repeat part (a) using a genetic algorithm instead of hill climbing.

# Part a - Hill-climbing algorithm implementation to solve TSPs:

# Important Notes:

# As described in the textbook, each state in the
# hill climbing search algorithm has all the components that make up a
# solution even if the current state is not the solution itself
# (the components are not in the right order in the case of tsp).
# In this case, each state contains the current path that travels through all nodes
# in the tsp as well as the length of that path.
# We have found the solution when we have reached a goal state,
# which is the path that visits all nodes/cities exactly once and returns to the starting node and has the shortest length.
# This means that we need to begin by generating an initial path
# that visits all nodes at random.

import random


class HillClimbingSolverForTSP:

    def __init__(self, tsp_problem):
        self.tsp_problem = tsp_problem

    def get_node_list(self):
        return list(self.tsp_problem.keys())

    def generate_initial_path(self):
        node_list = self.get_node_list()
        initial_path = []
        starting_node = ''
        for i in range(len(node_list)):
            if i == 0:
                starting_node = node_list[random.randint(0, (len(node_list) - 1))]
                initial_path.append(starting_node)
                node_list.remove(starting_node)
            else:
                placeholder_node = node_list[random.randint(0, (len(node_list) - 1))]
                initial_path.append(placeholder_node)
                node_list.remove(placeholder_node) #Remove the placeholder_node from the node_list to guarantee that the initial_path will contain a list of all nodes with no duplicates.
        initial_path.append(starting_node)
        return initial_path

    def calculate_path_length(self, path):
        path_length = 0
        node_list = self.get_node_list()
        for i in range(len(path)):
            if path[i] in node_list:
                if i < len(path) - 1:
                    graph_edge_list = self.tsp_problem[path[i]]
                    graph_edge =
                    path_length += self.tsp_problem[]


    def run_hill_climbing_algorithm(self):
        path = self.generate_initial_path()


# A GraphSegment class that creates an object that puts together the following information:
# a starting node, ending node, and the distance from the starting node to the ending node.
class GraphEdge:

    def __init__(self, starting_node, ending_node, distance):
        self.starting_node = starting_node
        self.ending_node = ending_node
        self.distance = distance


# Part b - Genetic algorithm implementation to solve TSPs:


# Test data used to test both the hill-climbing and genetic algorithm implementations:

# part a test data:
traveling_sales_person_graph_1 = {
    'A': [GraphEdge('A', 'B', 40), GraphEdge('A', 'C', 60), GraphEdge('A', 'D', 10)],
    'B': [GraphEdge('B', 'A', 40), GraphEdge('B', 'C', 50), GraphEdge('B', 'D', 20)],
    'C': [GraphEdge('C', 'A', 60), GraphEdge('C', 'B', 50), GraphEdge('C', 'D', 30)],
    'D': [GraphEdge('D', 'A', 10), GraphEdge('D', 'B', 20), GraphEdge('D', 'C', 30)]
}

hill_climbing_test_1 = HillClimbingSolverForTSP(traveling_sales_person_graph_1)
hill_climbing_test_1.run_hill_climbing_algorithm()

# part b test data:
