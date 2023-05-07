from math import ceil


def transition_function_shuffle():
    pass


def transition_function_swap():
    pass


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
    # TODO decide if we want to return the new solution

    return solution, solution_length
