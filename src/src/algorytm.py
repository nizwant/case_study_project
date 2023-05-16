from datetime import time, datetime

import numpy as np
from src.parserTSP import parse
import math
import random
import copy

def init_sol_func(distances):
    """
        Finds a suboptimal solution to the asymmetric Traveling Salesman Problem (TSP) using the nearest neighbor
    algorithm.
    It is irrelevant what values are on the diagonal of the matrix

    :param distances: list:
            N-dimensional asymmetric matrix of distances between points.

    :return: list:
            A list of integers representing the order in which cities should be visited to obtain a suboptimal
            solution to the TSP. The first city in the path is always city 0.
    """
    n = distances.shape[0]
    unvisited = set(range(1, n))
    path = [0]
    current_city = 0
    while unvisited:
        nearest_neighbor = min(unvisited, key=lambda city: distances[current_city][city])
        unvisited.remove(nearest_neighbor)
        path.append(nearest_neighbor)
        current_city = nearest_neighbor
    return path


def path_length(path, distances):
    """
        Calculates the total length of a path for a given TSP instance, taking into account that the path must
    return from the last city to the first city.

    :param path: list:
            A list of integers representing the order in which cities should be visited. The first and last
            cities in the path should be the same, i.e., path[0] == path[-1].
    :param distances: list:
            A square matrix of distances between cities. The element at index (i, j) represents the distance
            between city i and city j.

    :return:
            float:
            The total length of the path, including the distance from the last city back to the first city.
    """
    length = 0
    for i in range(len(path) - 1):
        length += distances[path[i], path[i + 1]]
    length += distances[path[-1], path[0]]
    return length


def pick_city(distances, current_city, max_distance):
    """
            Picks a random city from the neighborhood of the current city, given a distance matrix and a maximum
        distance defining the neighbourhood.
        If the neighbourhood is empty returns current city.

        :param distances: list:
                A distance matrix between cities.
        :param current_city: int:
                The index of the current city.
        :param max_distance: float:
                The maximum distance from the current city to consider.
        :return:
                integer:
                An integer representing the index of the randomly picked city.
    """

    n = distances.shape[0]
    candidate_cities = []

    for i in range(n):
        if i != current_city and distances[current_city, i] <= max_distance:
            candidate_cities.append(i)

    if len(candidate_cities) == 0:
        return current_city  # No suitable city found, return current city

    return random.choice(candidate_cities)  # Pick a random candidate city


def pick_adjacent(path, city):
    """
                Picks a random adjacent city on a path.

            :param path: list:
                    A path of the cities.
            :param city: int:
                    The index of the current city.
            :return:
                    integer:
                    An integer representing the name of the randomly picked city.
        """
    index_of_num = path.index(city)
    adj_numbers = [index_of_num - 1, (index_of_num + 1) % len(path)]
    return path[random.choice(adj_numbers)]

def fourth_city(t1, t2, t3, path):
    """
                Picks a city connected to t2 on a path. t4 cannot be on a path between t2 and t3 containing t1.

            :param t1: integer:
                    First city of the two-change algorithm.
            :param t2: integer:
                    Second city of the two-change algorithm.
            :param t3: integer:
                    Third city of the two-change algorithm.
            :param path: list:
                    List representing current path.
            :return:
                    integer:
                    An integer representing the name of the fourth city.
        """
    t1_index = path.index(t1)
    t2_index = path.index(t2)
    t3_index = path.index(t3)
    # cases: t1 t3 ... t2 and t2 ... t1 t3
    if (t2_index > t1_index and t3_index>t1_index) or (t3_index>t1_index and t2_index<t1_index):
        t4_index = t2_index-1
    # cases: t3 t1 ... t2 and t2 ... t3 t1
    if (t2_index > t1_index and t3_index<t1_index) or (t3_index<t1_index and t2_index<t1_index):
        t4_index = t2_index+1
    #TODO co jesli nie sa spelnione warunki i czy moze tak sie zdarzyc
    t4_index = t4_index % len(path)
    return path[t4_index]

def reverse_subarray(arr, start_idx, end_idx):
    """
    Reverses the order of elements in the subarray of arr from start_idx to end_idx (inclusive).
    """
    # swap elements until we reach the middle of the subarray
    while start_idx < end_idx:
        arr[start_idx], arr[end_idx] = arr[end_idx], arr[start_idx]
        start_idx += 1
        end_idx -= 1
    return arr

def two_change(t1, t2, t3, t4, path):
    """
                Deletes links between t1 -> t3 and t2 -> t4. Reverses order between two middle indices (on the path in graph not an array)
            For example in path: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 if we have choosen 1 -> 2 and 5 -> 6 the result will be
            a path with reversed order between 2 and 5: 1 -> 5 -> 4 -> 3 -> 2 -> 6 -> 7 .

            :param t1: integer:
                    First city of the two-change algorithm.
            :param t2: integer:
                    Second city of the two-change algorithm.
            :param t3: integer:
                    Third city of the two-change algorithm.
            :param t3: integer:
                    Third city of the two-change algorithm.
            :param path: list:
                    List representing current path.
            :return:
                    List:
                    Modified, partially reversed path (uses a deepcopy).
           """
    t1_index = path.index(t1)
    t2_index = path.index(t2)
    t3_index = path.index(t3)
    t4_index = path.index(t4)
    indices = [t1_index, t2_index, t3_index, t4_index]
    indices.sort()
    if indices[0]==0 and indices[1]!=1:
        middle_index_1 = indices[2]
        middle_index_2 = indices[3]
    else:
        middle_index_1 = indices[1]
        middle_index_2 = indices[2]
    modified_path = reverse_subarray(copy.deepcopy(path), middle_index_1, middle_index_2)
    return modified_path



def trial_move(path):
    """
        Implements algorithm modifying a path.
        !!! neighbourhood distance only for this matrix!!!
    :param path: list
        List of cities, which represent a path.
    :return:
        Modified list of cities representing a path.
    """
    # TODO which cities are in a neighbourhood - in paper 2.5/n^(1/2) but here it doesnt make sense (they used square 1x1) - maybe we should scale our matrix?
    # 125 is only for ftv38, 2.5*largest_dist/n^(1/2)
    neighbourhood_dist = 125

    # numbers t1, t2, t3, t4 represent cities not indices
    t1 = path[random.randint(0, len(path) - 1)]
    t2 = pick_city(distances, t1, neighbourhood_dist)
    t3 = pick_adjacent(path, t1)
    t4 = fourth_city(t1, t2, t3, path)
    modified_path = two_change(t1, t2, t3, t4, path)
    return modified_path


def metropolis_method(path, distances, temperature):
    """
        Implements metropolis method of modifying a path used in parallel tempering algorithm.
    :param path: list:
        List of cities which form a path.
    :param distances: list:
        N-dimensional matrix of distances between cities.
    :param temperature: float:
        Temperature which affects the probability of swaping current path with a longer one.
    :return:
        Modified path.
    """
    initial_energy = path_length(path, distances)
    modified_path = trial_move(path)
    modified_energy = path_length(modified_path, distances)
    acceptance_probability = math.exp(-(modified_energy-initial_energy)/temperature)
    epsilon = random.uniform(0, 1)
    if epsilon < min(1, acceptance_probability):
        path = modified_path
    return path


def PT_algorithm(distances, max_runtime, temperatures):
    """
        Implementation of parallel tempering algorithm for TSP (travelling salesman problem).
    :param distances: list:
        N-dimensional list of distances.
    :param max_runtime: integer:
        Number of seconds after this algorithm will give a solution.
    :param temperatures: list:
        List of temperatures for each replica.
    :return:
        Found solution.
    """
    # number of replicas
    num_tems = len(temperatures)
    # initialize solutions for each replica
    best_solution = init_sol_func(distances)
    current_solutions = [copy.deepcopy(best_solution) for _ in range(num_tems)]
    # variables which control the runtime of algorithm
    start_time = datetime.now()

# TODO te dystanse to moznaby jakos zapisac zeby tyle nie obliczac
    while (datetime.now() - start_time).total_seconds() < max_runtime:
        for i in range(num_tems):
            # change replica with metropolis method
            current_solutions[i] = metropolis_method(current_solutions[i], distances, temperatures[i])
            # update best solution
            if path_length(current_solutions[i], distances) < path_length(best_solution, distances):
                best_solution = copy.deepcopy(current_solutions[i])

        # temperature exchange between replicas with certain probability
        for i in range(num_tems-1):
            beta = (1/temperatures[i]) - (1/temperatures[i+1])
            difference_energy = path_length(current_solutions[i], distances) - path_length(current_solutions[i+1], distances)

    # TODO swap_prob nie wychodzi - za duze
            # swap_prob = min(np.exp(beta * difference_energy), 1)
            swap_prob = 0.5
            epsilon = random.uniform(0, 1)
            if epsilon < swap_prob:
                temperatures[i], temperatures[i+1] = temperatures[i+1], temperatures[i]

    return best_solution

'''
not important 
'''
def init_sol_func_test():
    distances = np.array([[0, 10, 15, 20], [5, 0, 35, 25], [30, 35, 0, 30], [20, 25, 30, 0]])
    path = init_sol_func(distances)
    print(path)


def find_second_largest(matrix):
    """
    Finds the second largest value in a matrix.
    """
    largest = matrix[0, 0]
    second_largest = None

    for value in matrix.flatten():
        if value > largest:
            second_largest = largest
            largest = value
        elif value != largest and (second_largest is None or value > second_largest):
            second_largest = value

    if second_largest is None:
        raise ValueError("Matrix has only one unique value")

    return second_largest

''' test '''

# distances = np.array([[0, 10, 15, 20], [5, 0, 35, 25], [30, 35, 0, 30], [20, 25, 30, 0]])
# path = init_sol_func(distances)
# print(distances)
# print(path)
# print(path_length(path, distances))

name = "ftv38.atsp"
distances=parse(name)
# print(distances)
# max_dis=find_second_largest(parse(name))
# print(max_dis)
# print(len(parse(name)))
#
# # pick city test
# print(pick_city(distances, 2, 125))
path = init_sol_func(distances)
# print(path)
# print(trial_move(path))
# for i in range (100):
#     path = metropolis_method(path, distances, 0.045)
#     print(path_length(path, distances))
temperatures = [1.5 / math.sqrt(39), 1 / math.sqrt(39), 2 / math.sqrt(39), 0.5 / math.sqrt(39)]
max_runtime = 30

random.seed(123)
print(path_length(PT_algorithm(distances, max_runtime, temperatures), distances))

distances = np.array([[0, 10, 15, 20], [5, 0, 35, 25], [30, 35, 0, 30], [20, 25, 30, 0]])
print(path_length(PT_algorithm(distances, max_runtime, temperatures), distances))


