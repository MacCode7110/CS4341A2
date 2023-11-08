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

# Referenced GeeksForGeeks for travelling salesperson problem definition
# and coded the edges from the top graph example for the
# second graph test configuration: https://www.geeksforgeeks.org/travelling-salesman-problem-using-dynamic-programming/

# MST heuristic and state space:

# As described in the textbook, each state in the
# hill climbing search algorithm can have all the components that make up a
# solution even if the current state is not the solution itself
# (the components or nodes are not in the right order in the case of tsp).

# Furthermore, this supports the fact that we are using the MST heuristic, which states the following:
# The traveling salesperson problem (TSP) can be solved with the minimum-spanning tree (MST) heuristic,
# which estimates the cost of completing a tour, given that a partial tour
# has already been constructed. The MST cost of a set of cities is the smallest sum of the link
# costs of any tree that connects all the cities.
# In this case, each state contains the current path that travels through all nodes
# in the tsp as well as the length of that path.

# Immediate neighbor states:

# Immediate neighbor states are distinguished by and compared through
# their path length value. The path length values of neighboring states are calculated by changing which edges are
# traveled along between the nodes in the current state (essentially, the way this works is that
# every successive pair of nodes (where a pair starts with the node that was previously the second item in a pair)
# swap positions in a list excluding the starting node
# that appears at the end of the list (which represents the completion of a tour)).

# Goal state and initial path generation:

# We have found the solution when we have reached a goal state,
# which is the path that visits all nodes/cities exactly once
# and returns to the starting node and has the shortest length.
# This means that we need to begin by generating an initial path
# that visits all nodes at random to begin comparing against in the run_hill_climbing_algorithm function.

import random


class HillClimbingSolverForTSP:

    def __init__(self, tsp_problem,  problem_configuration_number):
        self.tsp_problem = tsp_problem
        self.problem_configuration_number = problem_configuration_number

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
                node_list.remove(
                    placeholder_node)  # Remove the placeholder_node from the node_list to
                # guarantee that the initial_path will contain a list of all nodes with no duplicates.
        initial_path.append(starting_node)
        return initial_path

    def generate_all_immediate_neighbor_paths(self, current_path):
        neighbor_path_list = []
        for i in range(len(current_path)):
            neighbor_path = current_path.copy()  # Need to copy the current_path
            # array over to the neighbor_path array at the start of each new iteration.
            if i < len(current_path) - 2:
                neighbor_path[i] = current_path[i + 1]
                neighbor_path[i + 1] = current_path[i]
                if i == 0:
                    neighbor_path[len(neighbor_path) - 1] = neighbor_path[0]
                neighbor_path_list.append(neighbor_path)
        return neighbor_path_list

    def get_shortest_neighbor_path(self, neighbor_path_list):
        neighbor_path_length_list = []
        for i in neighbor_path_list:
            neighbor_path_length_list.append(self.calculate_path_length(i))

        return neighbor_path_list[neighbor_path_length_list.index(min(neighbor_path_length_list))]

    def get_graph_edge_object(self, end_node, graph_edge_list):
        for i in range(len(graph_edge_list)):
            if graph_edge_list[i].ending_node == end_node:
                return graph_edge_list[i]

    def calculate_path_length(self, path):
        path_length = 0
        node_list = self.get_node_list()
        for i in range(len(path)):
            if path[i] in node_list:
                if i < len(path) - 1:
                    graph_edge_list = self.tsp_problem[path[i]]
                    graph_edge_object = self.get_graph_edge_object(path[i + 1], graph_edge_list)
                    path_length += graph_edge_object.distance
        return path_length

    def run_hill_climbing_algorithm(self):
        path = self.generate_initial_path()
        path_length = self.calculate_path_length(path)
        neighbor_path_list = self.generate_all_immediate_neighbor_paths(path)
        shortest_neighbor_path = self.get_shortest_neighbor_path(neighbor_path_list)

        while path_length > self.calculate_path_length(shortest_neighbor_path):
            path = shortest_neighbor_path
            path_length = self.calculate_path_length(shortest_neighbor_path)
            neighbor_path_list = self.generate_all_immediate_neighbor_paths(path)
            shortest_neighbor_path = self.get_shortest_neighbor_path(neighbor_path_list)

        print("The shortest path that visits each node exactly once and returns to the starting node "
              "for Traveling Salesmen Problem Configuration " + str(self.problem_configuration_number) + " is " +
              "".join(path) +
              " with a length of " + str(path_length))


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

'''
# Test Configuration 1
traveling_sales_person_graph_1 = {
    'A': [GraphEdge('A', 'B', 40), GraphEdge('A', 'C', 60), GraphEdge('A', 'D', 10)],
    'B': [GraphEdge('B', 'A', 40), GraphEdge('B', 'C', 50), GraphEdge('B', 'D', 20)],
    'C': [GraphEdge('C', 'A', 60), GraphEdge('C', 'B', 50), GraphEdge('C', 'D', 30)],
    'D': [GraphEdge('D', 'A', 10), GraphEdge('D', 'B', 20), GraphEdge('D', 'C', 30)]
}

hill_climbing_test_1 = HillClimbingSolverForTSP(traveling_sales_person_graph_1, 1)
hill_climbing_test_1.run_hill_climbing_algorithm()

# Test Configuration 2
traveling_sales_person_graph_2 = {
    'A': [GraphEdge('A', 'B', 10), GraphEdge('A', 'C', 20), GraphEdge('A', 'D', 15)],
    'B': [GraphEdge('B', 'A', 10), GraphEdge('B', 'C', 25), GraphEdge('B', 'D', 35)],
    'C': [GraphEdge('C', 'A', 20), GraphEdge('C', 'B', 25), GraphEdge('C', 'D', 30)],
    'D': [GraphEdge('D', 'A', 15), GraphEdge('D', 'B', 35), GraphEdge('D', 'C', 30)]
}

hill_climbing_test_2 = HillClimbingSolverForTSP(traveling_sales_person_graph_2, 2)
hill_climbing_test_2.run_hill_climbing_algorithm()
'''

# Test Configuration 3
traveling_sales_person_graph_3 = {
    'A': [GraphEdge('A', 'B', 10), GraphEdge('A', 'C', 20)],
    'B': [GraphEdge('B', 'A', 10), GraphEdge('B', 'C', 25), GraphEdge('B', 'D', 35)],
    'C': [GraphEdge('C', 'A', 20), GraphEdge('C', 'B', 25), GraphEdge('C', 'D', 30)],
    'D': [GraphEdge('D', 'B', 35), GraphEdge('D', 'C', 30)]
}

hill_climbing_test_3 = HillClimbingSolverForTSP(traveling_sales_person_graph_3, 3)
hill_climbing_test_3.run_hill_climbing_algorithm()

# part b test data:
