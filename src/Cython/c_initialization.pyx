from math import floor
from random import choice
from random import random
from random import shuffle

from numpy.random import beta
import numpy

from c_calculate_distance import cycle_length


def initialize_temperatures(
        n: int, min: float, max: float, a: float = 1, b: float = 1
) -> numpy.ndarray:
    """
    Returns a list of n temperatures between min and max,
    with a and b as parameters for the beta distribution.
    if a = b = 1, the temperatures are uniformly distributed between min and max.
    """
    # modification to consider: adding distribution type as parameter
    # or different approach: according to the paper below, it's good to set initial temperatures
    # as standard deviation of initial value of cost function (our initial solution lengths)
    # https://www.researchgate.net/publication/220403361_Metaheuristics_can_solve_Sudoku_puzzles
    # ~ Marta
    return beta(a, b, n) * (max - min) + min


def initialize_transition_function_types(n: int, probability_of_shuffle: float) -> list:
    """
    Returns a bool list of length n, where
    q[i] = True means that the transition
    function at index i is a shuffle transition function.
    """
    return [random() < probability_of_shuffle for _ in range(n)]


def initialize_initial_solutions(
    n: int, distance_matrix: list[list[float]], probability_of_heuristic: float
) -> tuple:
    """
    Returns a list of n solutions, where
    q[i] has probability_of_heuristic chance of being a heuristic initial solution.
    heuristic used here is nearest neighbor.
    """
    # calculate nearest neighbor solution only once
    nearest_neighbor_solution = better_nearest_neighbor_initial_solution(
        distance_matrix
    )

    # create initial solution list and fill it with
    # either nearest neighbor solution or random solution
    initial_solutions = [None for _ in range(n)]
    initial_solutions_lengths = [None for _ in range(n)]
    for i in range(n):
        if random() < probability_of_heuristic:
            initial_solutions[i] = choice(nearest_neighbor_solution)
        else:
            initial_solutions[i] = random_initial_solution(distance_matrix)
        initial_solutions_lengths[i] = cycle_length(
            initial_solutions[i], distance_matrix
        )
    return initial_solutions, initial_solutions_lengths


def better_nearest_neighbor_initial_solution(
    distance_matrix: list[list[float]],
) -> list:
    """
    Finds a suboptimal solution to the asymmetric Traveling Salesman Problem
    It is irrelevant what values are on the diagonal of the matrix

    :return: list:
            A list of integers representing the order in which
            cities should be visited to obtain a suboptimal
            solution to the TSP.
    """

    number_of_cites = len(distance_matrix)
    heuristic_solutions = [None for _ in range(number_of_cites)]

    for starting_city in range(number_of_cites):
        unvisited = set(range(number_of_cites))

        # set starting city
        current_city = starting_city
        path = [current_city]
        unvisited.remove(current_city)

        while unvisited:
            nearest_neighbor = min(
                unvisited, key=lambda city: distance_matrix[current_city][city]
            )
            unvisited.remove(nearest_neighbor)
            path.append(nearest_neighbor)
            current_city = nearest_neighbor
        heuristic_solutions[starting_city] = path

    # select only best 10% of solutions
    heuristic_solutions.sort(
        key=lambda solution: cycle_length(solution, distance_matrix)
    )
    best_heuristic_solutions = heuristic_solutions[: floor(number_of_cites * 0.1)]
    return best_heuristic_solutions


def random_initial_solution(distance_matrix: list[list[float]]) -> list:
    """
    Finds a completely random solution to the asymmetric Traveling Salesman Problem

    :return: list:
        A list of integers representing the order in which cities should be visited
    """
    size = len(distance_matrix)
    solution = list(range(size))
    shuffle(solution)
    return solution


def initialization(
    distance_matrix: list[list[float]],
    n: int,
    min_temperature: float,
    max_temperature: float,
    probability_of_shuffle: float,
    probability_of_heuristic: float,
    a: float,
    b: float,
) -> tuple:
    """
    Returns a tuple of lists, where
    the first list is a list of n temperatures between min_temperature and max_temperature,
    with a and b as parameters for the beta distribution.
    the second list is a bool list of length n, where
    q[i] = True means that the transition
    function at index i is a shuffle transition function,
    the third list is a list of n initial solutions, where
    q[i] has probability_of_heuristic chance of being a heuristic initial solution.
    """
    temperatures = initialize_temperatures(n, min_temperature, max_temperature, a, b)
    transition_function_types = initialize_transition_function_types(
        n, probability_of_shuffle
    )
    initial_solutions, initial_solutions_lengths = initialize_initial_solutions(
        n, distance_matrix, probability_of_heuristic
    )

    return (
        temperatures,
        transition_function_types,
        initial_solutions,
        initial_solutions_lengths,
    )