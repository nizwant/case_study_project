from time import time

from initialization import initialization
from metropolis_transition import metropolis_transition
from src.Code.cooling import cooling
from src.Code.replica_transition import replica_transition


def pt_sa(
        distance_matrix: list[list[float]],
        n: int,
        min_temperature: float,
        max_temperature: float,
        probability_of_shuffle: float,
        probability_of_heuristic: float,
        a: float,
        b: float,
        duration_of_execution_in_seconds: int,
        k: int,
        max_length_percent_of_cycle: float,
        swap_states_probability: float,
        closeness: float,
        cooling_rate: float
) -> tuple[list[int], float]:
    """
    Performs a Parallel Tempering Simulated Annealing
    algorithm on a given distance matrix.
    """
    start = time()
    best_solution = [None for _ in range(len(distance_matrix))]
    best_solution_length = float("inf")
    solutions_length = [float("inf") for _ in range(n)]

    temperatures, transition_function_types, solutions = initialization(
        distance_matrix,
        n,
        min_temperature,
        max_temperature,
        probability_of_shuffle,
        probability_of_heuristic,
        a,
        b,
    )

    while time() - start < duration_of_execution_in_seconds:
        for _ in range(k):
            for state in range(n):  # potential multithreading
                solutions[state], solutions_length[state] = metropolis_transition(
                    solutions[state],
                    solutions_length[state],
                    distance_matrix,
                    temperatures[state],
                    max_temperature,
                    transition_function_types[state],
                    max_length_percent_of_cycle,
                )

                if solutions_length[state] < best_solution_length:
                    best_solution, best_solution_length = (
                        solutions[state],
                        solutions_length[state],
                    )

            for _ in range(n):
                temperatures = replica_transition(swap_states_probability,
                                                  closeness,
                                                  temperatures,
                                                  solutions_length,
                                                  best_solution_length,
                                                  n)

        for state in range(n):
            temperatures[state] = cooling(cooling_rate, temperatures[state])

    return best_solution, best_solution_length
