import warnings
from math import ceil
from random import randrange
from random import shuffle
from random import uniform

import numpy as np

from c_calculate_distance import cycle_length


def transition_function_shuffle(
        solution: list[int],
        solution_length: float,
        distance_matrix: list[list[float]],
        transformation_length: int,
) -> tuple[list[int], float]:
    """
    Performs a shuffle transition on a given solution.
    transformation_length is the length of the transformation.
    i.e. transformation_length = 3 means that we will
    shuffle path with length 3

    if we have a path [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    and starting index is 9, then we will shuffle list [9, 10, 1]
    and paste it back to the original list with solution
    """
    if transformation_length < 2:
        # minimum length of this transformation that make sense is 2
        transformation_length = 2

    list_to_shuffle = [None for _ in range(transformation_length)]
    l = len(solution)
    start_index = randrange(l)
    for i in range(transformation_length):
        list_to_shuffle[i] = solution[(start_index + i) % l]

    shuffle(list_to_shuffle)

    new_solution = solution.copy()
    for i in range(transformation_length):
        new_solution[(start_index + i) % l] = list_to_shuffle[i]

    new_solution_length = cycle_length(new_solution, distance_matrix)
    return new_solution, new_solution_length


def transition_function_swap(
        solution: list[int],
        solution_length: float,
        distance_matrix: list[list[float]],
        transformation_length: int,
) -> tuple[list[int], float]:
    """
    Performs a swap transition on a given solution.
    transformation_length is the length of the transformation.
    i.e. transformation_length = 3 means that we will
    swap two paths with length 3.

    Let's say we have a solution [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
    If we draw starting cities 2 and 6, then we swap paths [2, 3, 4] and [6, 7, 8].
    If we draw starting cities 5 and 6, then we swap paths [3, 4, 5] and [6, 7, 8].
    If we draw starting cities 1 and 10, then we swap paths [1, 2, 3] and [8, 9, 10].
    """
    if transformation_length < 1:
        # minimum length of this transformation that make sense is 1
        transformation_length = 1

    l = len(solution)

    start_index_first_path = randrange(l)

    # starting indices need to be different
    while True:
        start_index_second_path = randrange(l)
        if start_index_second_path != start_index_first_path:
            break

    # first path should be actually first
    if start_index_second_path < start_index_first_path:
        start_index_first_path, start_index_second_path = start_index_second_path, start_index_first_path

    first_path_can_go_right = start_index_second_path - start_index_first_path >= transformation_length
    second_path_can_go_right = l - start_index_second_path + start_index_first_path >= transformation_length

    if (not first_path_can_go_right) and second_path_can_go_right:
        start_index_first_path = start_index_first_path - transformation_length + 1

    elif first_path_can_go_right and (not second_path_can_go_right):
        start_index_second_path = start_index_second_path - transformation_length + 1

    first_path = range(start_index_first_path, start_index_first_path + transformation_length)
    second_path = range(start_index_second_path, start_index_second_path + transformation_length)

    new_solution = solution.copy()
    for i, j in zip(first_path, second_path):
        new_solution[i % l], new_solution[j % l] = new_solution[j % l], new_solution[i % l]

    new_solution_length = cycle_length(new_solution, distance_matrix)
    return new_solution, new_solution_length


def acceptance(
        solution_length: float,
        new_solution_length: float,
        temperature: float
) -> bool:
    """
    Decides whether to accept the new solution.
    """
    warnings.filterwarnings("ignore")
    acceptance_probability = np.exp(-(new_solution_length - solution_length) / temperature)
    return uniform(0, 1) < min(1.0, acceptance_probability)


def metropolis_transition(
        solution: list[int],
        solution_length: float,
        distance_matrix: list[list[float]],
        temperature: float,
        max_possible_temperature: float,
        is_shuffle: bool,
        max_length_percent_of_cycle: float,
) -> tuple[list[int], float]:
    """
    Performs a Metropolis transition on a given solution.
    ratio = (temperature / max_possible_temperature) determines the length
    passed to the transition function. The length is a percentage
    ratio from max_length_percent_of_cycle.
    if is_shuffle is True, then the transition function is transition_function_shuffle
    else the transition function is transition_function_swap
    """
    ratio = temperature / max_possible_temperature
    transformation_length = ceil(max_length_percent_of_cycle * len(solution) * ratio)

    if is_shuffle:
        new_solution, new_solution_length = transition_function_shuffle(
            solution, solution_length, distance_matrix, transformation_length
        )
    else:
        new_solution, new_solution_length = transition_function_swap(
            solution, solution_length, distance_matrix, transformation_length
        )

    if acceptance(solution_length, new_solution_length, temperature):
        return new_solution, new_solution_length

    return solution, solution_length