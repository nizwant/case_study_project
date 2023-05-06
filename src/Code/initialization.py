from numpy.random import beta
from random import random


def initialize_temperatures(
    n: int, min: float, max: float, a: float = 1, b: float = 1
) -> list:
    """
    Returns a list of n temperatures between min and max,
    with a and b as parameters for the beta distribution.
    if a = b = 1, the temperatures are uniformly distributed between min and max.
    """
    return beta(a, b, n) * (max - min) + min


def initialize_transition_function_type(n: int, probability_of_shuffle: float) -> list:
    """
    Returns a bool list of length n, where
    q[i] = True means that the transition
    function at index i is a shuffle transition function.
    """
    return [random.random() < probability_of_shuffle for _ in range(n)]


def initialize_initial_solution(
    n: int, distance_matrix: float, probability_of_heuristic: float
) -> list:
    """
    Returns a list of n solutions, where
    q[i] has probability_of_heuristic chance of being a heuristic initial solution.
    heuristic used here is nearest neighbor.
    """
    nearest_neighbor_solution = nearest_neighbor_initial_solution(distance_matrix)

    return [random.random() < probability_of_heuristic for _ in range(n)]


def nearest_neighbor_initial_solution(distance_matrix: float) -> list:
    """
    Finds a suboptimal solution to the asymmetric Traveling Salesman Problem (TSP)
    It is irrelevant what values are on the diagonal of the matrix

    :return: list:
            A list of integers representing the order in which cities should be visited to obtain a suboptimal
            solution to the TSP. The first city in the path is always city 0.
    """
    size = distance_matrix.shape[0]
    unvisited = set(range(1, size))
    path = [0]
    current_city = 0
    while unvisited:
        nearest_neighbor = min(
            unvisited, key=lambda city: distance_matrix[current_city][city]
        )
        unvisited.remove(nearest_neighbor)
        path.append(nearest_neighbor)
        current_city = nearest_neighbor
    return path


def random_initial_solution():
    pass
