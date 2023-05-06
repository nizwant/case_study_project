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


def initialize_initial_solution(n: int, probability_of_heuristic: float) -> list:
    """
    Returns a list of n solutions, where
    q[i] has probability_of_heuristic chance of being a heuristic initial solution.
    heuristic used here is nearest neighbor.
    """
    # zapisac raz rozwiazanie nearest neighbor i potem je kopiowac
    # stworzyc funkcje nearest neighbor
    # stworzyc funkcje random initial solution
    return [random.random() < probability_of_heuristic for _ in range(n)]
