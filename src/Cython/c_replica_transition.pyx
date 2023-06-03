from random import randrange, uniform
import numpy

def replica_transition(
        swap_states_probability: float,
        closeness: float,
        temperatures: list[float],
        solutions_length: list[float],
        best_solution_length: float,
        n: int
) -> numpy.ndarray:
    """
    Perform replica transition on given states.
    swap_states_probability is probability of swapping states.
    closeness defines factor of maximum solution length that we consider close to the best solution.
    """
    first_index = randrange(n)

    while True:
        second_index = randrange(n)
        if second_index != first_index:
            break
    first_solution_close_to_best = solutions_length[first_index] <= closeness * best_solution_length
    second_solution_close_to_best = solutions_length[second_index] <= closeness * best_solution_length

    if first_solution_close_to_best or second_solution_close_to_best:
        pass

    elif uniform(0, 1) < swap_states_probability:
        temperatures[first_index], temperatures[second_index] = temperatures[second_index], temperatures[first_index]

    return temperatures
