from math import ceil
from random import randrange
from random import shuffle
from calculate_distance import cycle_length


def transition_function_shuffle(
    solution: list[int],
    solution_length: float,
    distance_matrix: list[list[float]],
    transformation_length: int,
) -> tuple[list[int], float]:
    """
    Performs a shuffle transition on a given solution.
    transformation_length is the length of the transformation.
    ie. transformation_length = 3 means that we will
    shuffle path with length 3

    if we have a path [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    and starting index is 9, then we will shuffle list [9, 10, 1]
    and paste it back to the original list with solution
    """
    if transformation_length < 2:
        # minimum length of this transformation that make sense is 2
        transformation_length = 2

    list_to_shuffle = [None for _ in range(transformation_length)]
    start_index = randrange(len(solution))
    for i in range(transformation_length):
        list_to_shuffle[i] = solution[(start_index + i) % len(solution)]

    shuffle(list_to_shuffle)

    new_solution = solution.copy()
    for i in range(transformation_length):
        new_solution[(start_index + i) % len(solution)] = list_to_shuffle[i]

    new_solution_length = cycle_length(new_solution, distance_matrix)
    return new_solution, new_solution_length


def transition_function_swap(
    solution: list[int],
    solution_length: float,
    distance_matrix: list[list[float]],
    transformation_length: int,
) -> tuple[list[int], float]:
    pass
    # TODO: implement transition_function_swap


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
    # TODO function that decides if we want to return the new solution

    return solution, solution_length
