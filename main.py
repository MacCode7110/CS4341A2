# Chapter 4 Exercise 4.3

# In this exercise, we explore the use of local search methods to solve TSPs of the type defined in Exercise 3.30.

# Exercise 3.30 Description:

# The traveling salesperson problem (TSP) can be solved with the minimum-spanning tree (MST) heuristic,
# which estimates the cost of completing a tour, given that a partial tour
# has already been constructed. The MST cost of a set of cities is the smallest sum of the link
# costs of any tree that connects all the cities.

# a. Implement and test a hill-climbing method to solve TSPs.
# b. Repeat part (a) using a genetic algorithm instead of hill climbing.

# ---------------

# Important notes for part a:

# Referenced GeeksForGeeks for travelling salesperson problem definition
# and coded the edges from the top graph example for the
# second graph test configuration: https://www.geeksforgeeks.org/travelling-salesman-problem-using-dynamic-programming/

# MST heuristic and state space:

# As described in the textbook, each state in the
# hill climbing search algorithm can have all the components that make up a
# solution even if the current state is not the solution itself
# (the components or nodes are not in the right order in the case of tsp).

# Furthermore, this supports the fact that we are using the MST heuristic, which I learned
# more about here: https://aswani.ieor.berkeley.edu/teaching/FA13/151/lecture_notes/ieor151_lec17.pdf
# The MST heuristic states the following in the textbook and applies to graph problems:
# The traveling salesperson problem (TSP) can be solved with the minimum-spanning tree (MST) heuristic,
# which estimates the cost of completing a tour, given that a partial tour
# has already been constructed. The MST cost of a set of cities is the smallest sum of the link
# costs of any tree that connects all the cities.
# Based on the information listed above, I have determined that each state contains the currently selected path
# that travels through all nodes in the tsp as well as the length of that path.

# Immediate neighbor states:

# Immediate neighbor states are distinguished by and compared through
# their path length value. The path length values of neighboring states are calculated by changing which edges are
# traveled along between the nodes in the current state. Essentially, the way this works is that
# every successive pair of nodes (where a pair starts with the node that was previously
# the second item in a pair generated prior) swap positions in a list. This swapping process excludes
# a copy of the starting node that appears at the end of the list (which represents the salesperson' return
# to the origin/starting city in the tour).
# For example, for cities A, B, C, D:
#   if the current state is path ABCDA, then the following paths would be immediate neighbor states:
#       a. BACDB <- A and B swap positions to form this new path.
#       b. ACBDA <- B and C swap positions to form this new path.
#       c. ABDCA <- C and D swap positions to form this new path.

# Goal state and initial path generation:

# We have found the solution when we have reached a goal state,
# which is the path that visits all nodes/cities exactly once
# and returns to the starting node and has the shortest length.
# This means that we need to begin by generating an initial path
# that visits all nodes at random to begin comparing against in the run_hill_climbing_algorithm function.

# Assumptions
#   a. For every tsp problem, each node must be connected to every other node through edges in the graph.

# ---------------

# Important notes for part b


# ---------------

# Part a - Hill-climbing algorithm implementation to solve TSPs:
import operator
import random


class HillClimbingSolverForTSP:

    def __init__(self, tsp_problem, problem_configuration_number):
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
            # array over to the neighbor_path array at the start of each new iteration to
            # generate a new immediate neighbor to the current_path.
            if i < len(current_path) - 2:
                neighbor_path[i] = current_path[i + 1]
                neighbor_path[i + 1] = current_path[i]
                if i == 0:
                    neighbor_path[len(neighbor_path) - 1] = neighbor_path[0]
                neighbor_path_list.append(neighbor_path)
        return neighbor_path_list

    # get_shortest_neighbor_path is where the MST heuristic for the tsp problem is implemented;
    # we find the minimum spanning tree, in other words the shortest path that
    # visits all nodes and returns to the origin/starting node.
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

        print("Hill Climbing Algorithm Output: The shortest path that visits each node "
              "exactly once and returns to the starting node "
              "for Traveling Salesmen Problem Configuration " + str(self.problem_configuration_number) + " is " +
              "".join(path) +
              " with a length of " + str(path_length))


# Part b - Genetic algorithm implementation to solve TSPs:

# Genetic algorithm steps followed below:
#   a. Initial population
#   b. Evaluation through fitness function
#   c. Selection
#   d. Crossover
#   e. Mutation

# State space:
# Each state contains the current generated path and the length of the path.
# A gene is a single node/city, and an individual is a tsp path made up of some number of genes.
# Initial population:
# A list of tsp paths randomly generated and used to start running the rest of the algorithm.
# Fitness score:
# The fitness score of each state corresponds to the length of the tsp path.
# In this case, the fitness score is calculated by subtracting the length of the tsp path from 100,
# which is a trivially chosen integer.
# Shorter tsp paths will have higher fitness scores and longer tsp paths will have lower fitness scores.
# Selection process:
# States selected to be parents of the next generation are selected from a list of paths with fitness scores
# using tournament selection: https://www.geeksforgeeks.org/tournament-selection-ga/
# From a random selection of n individuals from the population, the most fit individual is selected as a parent for the next generation of paths.
# This process is repeated twice so that two of the most fit parents from their respective group selections can then crossover.
# Crossover process:
# We randomly select a crossover point to split each of the parent strings (tsp paths).
# The parts are recombined to form two children paths, one with the
# first part of the path of parent 1 and the second part of the path of parent 2.
# The other with the second part of the path of parent 1 and the first part of the path of parent 2.
# Mutation process:
# Determines how often an offspring state has a random mutation to its tsp path.
# When an offspring has been generated, two cities in a tsp path swap positions
# with probability equal to the mutation rate.

class GeneticAlgorithmSolverForTSP:

    def __init__(self, tsp_problem, problem_configuration_number):
        self.tsp_problem = tsp_problem
        self.problem_configuration_number = problem_configuration_number

    def get_node_list(self):
        return list(self.tsp_problem.keys())

    def generate_individual_path(self):
        node_list = self.get_node_list()
        starting_node = ''
        individual_path = []
        for i in range(len(node_list)):
            if i == 0:
                starting_node = node_list[random.randint(0, (len(node_list) - 1))]
                individual_path.append(starting_node)
                node_list.remove(starting_node)
            else:
                placeholder_node = node_list[random.randint(0, (len(node_list) - 1))]
                individual_path.append(placeholder_node)
                node_list.remove(
                    placeholder_node)  # Remove the placeholder_node from the node_list to
                # guarantee that the initial_path will contain a list of all nodes with no duplicates.
        individual_path.append(starting_node)
        return individual_path

    def generate_initial_population(self):
        initial_population = []
        population_size = 10
        for i in range(population_size):
            initial_population.append(self.generate_individual_path())
        return initial_population

    def select_parent_paths(self, population_fitness_score_dictionary_list):
        population_fitness_score_dictionary_list_copy = []
        selected_parent_paths_and_fitness_scores = []
        most_fit_parent_paths_and_fitness_scores = []
        selection_number = 5
        for i in range(2):
            population_fitness_score_dictionary_list_copy = population_fitness_score_dictionary_list.copy()
            for j in range(selection_number):
                dictionary = population_fitness_score_dictionary_list_copy[random.randint(0, (len(population_fitness_score_dictionary_list_copy)) - 1)]
                selected_parent_paths_and_fitness_scores.append(dictionary)
                population_fitness_score_dictionary_list_copy.remove(dictionary)

        return most_fit_parent_paths_and_fitness_scores

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

    def calculate_population_fitness_scores(self, population):
        population_fitness_score_dictionary_list = []
        for i in range(len(population)):
            population_fitness_score_dictionary_list.append(
                {population[i]: (100 - self.calculate_path_length(population[i]))})
        return population_fitness_score_dictionary_list

    def run_genetic_algorithm(self):
        path = self.generate_initial_population()
        population_fitness_score_dictionary_list = self.calculate_population_fitness_scores()
        most_fit_parent_paths = self.select_parent_paths(population_fitness_score_dictionary_list)

        print("Genetic Algorithm Output: The shortest path that visits each node "
              "exactly once and returns to the starting node "
              "for Traveling Salesmen Problem Configuration " + str(self.problem_configuration_number) + " is " +
              "".join(path) +
              " with a length of " + str(path_length))


# Test data used to test both the hill-climbing and genetic algorithm implementations:

# A GraphSegment class that creates an object that puts together the following information:
# a starting node, ending node, and the distance from the starting node to the ending node.
# This class is used to construct test data below.
class GraphEdge:

    def __init__(self, starting_node, ending_node, distance):
        self.starting_node = starting_node
        self.ending_node = ending_node
        self.distance = distance


# part a test data:

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

# Test Configuration 3
traveling_sales_person_graph_3 = {
    'A': [GraphEdge('A', 'B', 12), GraphEdge('A', 'C', 10), GraphEdge('A', 'D', 19), GraphEdge('A', 'E', 8)],
    'B': [GraphEdge('B', 'A', 12), GraphEdge('B', 'C', 3), GraphEdge('B', 'D', 7), GraphEdge('B', 'E', 2)],
    'C': [GraphEdge('C', 'A', 10), GraphEdge('C', 'B', 3), GraphEdge('C', 'D', 6), GraphEdge('C', 'E', 20)],
    'D': [GraphEdge('D', 'A', 19), GraphEdge('D', 'B', 7), GraphEdge('D', 'C', 6), GraphEdge('D', 'E', 4)],
    'E': [GraphEdge('E', 'A', 8), GraphEdge('E', 'B', 2), GraphEdge('E', 'C', 20), GraphEdge('E', 'D', 4)]
}

hill_climbing_test_3 = HillClimbingSolverForTSP(traveling_sales_person_graph_3, 3)
hill_climbing_test_3.run_hill_climbing_algorithm()

'''
# Test Configuration 4
traveling_sales_person_graph_4 = {
    'A': [GraphEdge('A', 'B', 10), GraphEdge('A', 'C', 20)],
    'B': [GraphEdge('B', 'A', 10), GraphEdge('B', 'C', 25), GraphEdge('B', 'D', 35)],
    'C': [GraphEdge('C', 'A', 20), GraphEdge('C', 'B', 25), GraphEdge('C', 'D', 30)],
    'D': [GraphEdge('D', 'B', 35), GraphEdge('D', 'C', 30)]
}

hill_climbing_test_3 = HillClimbingSolverForTSP(traveling_sales_person_graph_3, 3)
hill_climbing_test_3.run_hill_climbing_algorithm()
'''

# part b test data:

# Test Configuration 1
traveling_sales_person_graph_4 = {
    'A': [GraphEdge('A', 'B', 40), GraphEdge('A', 'C', 60), GraphEdge('A', 'D', 10)],
    'B': [GraphEdge('B', 'A', 40), GraphEdge('B', 'C', 50), GraphEdge('B', 'D', 20)],
    'C': [GraphEdge('C', 'A', 60), GraphEdge('C', 'B', 50), GraphEdge('C', 'D', 30)],
    'D': [GraphEdge('D', 'A', 10), GraphEdge('D', 'B', 20), GraphEdge('D', 'C', 30)]
}

genetic_algorithm_test_4 = GeneticAlgorithmSolverForTSP(traveling_sales_person_graph_4, 4)
genetic_algorithm_test_4.run_genetic_algorithm()

# Test Configuration 2
traveling_sales_person_graph_5 = {
    'A': [GraphEdge('A', 'B', 10), GraphEdge('A', 'C', 20), GraphEdge('A', 'D', 15)],
    'B': [GraphEdge('B', 'A', 10), GraphEdge('B', 'C', 25), GraphEdge('B', 'D', 35)],
    'C': [GraphEdge('C', 'A', 20), GraphEdge('C', 'B', 25), GraphEdge('C', 'D', 30)],
    'D': [GraphEdge('D', 'A', 15), GraphEdge('D', 'B', 35), GraphEdge('D', 'C', 30)]
}

genetic_algorithm_test_5 = GeneticAlgorithmSolverForTSP(traveling_sales_person_graph_5, 5)
genetic_algorithm_test_5.run_genetic_algorithm()

# Test Configuration 3
traveling_sales_person_graph_6 = {
    'A': [GraphEdge('A', 'B', 12), GraphEdge('A', 'C', 10), GraphEdge('A', 'D', 19), GraphEdge('A', 'E', 8)],
    'B': [GraphEdge('B', 'A', 12), GraphEdge('B', 'C', 3), GraphEdge('B', 'D', 7), GraphEdge('B', 'E', 2)],
    'C': [GraphEdge('C', 'A', 10), GraphEdge('C', 'B', 3), GraphEdge('C', 'D', 6), GraphEdge('C', 'E', 20)],
    'D': [GraphEdge('D', 'A', 19), GraphEdge('D', 'B', 7), GraphEdge('D', 'C', 6), GraphEdge('D', 'E', 4)],
    'E': [GraphEdge('E', 'A', 8), GraphEdge('E', 'B', 2), GraphEdge('E', 'C', 20), GraphEdge('E', 'D', 4)]
}

genetic_algorithm_test_6 = GeneticAlgorithmSolverForTSP(traveling_sales_person_graph_6, 6)
genetic_algorithm_test_6.run_genetic_algorithm()
