from initialization import initialization
from metropolis_transition import metropolis_transition
from time import time


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
) -> tuple[list[int], float]:
    start = time()
    best_solution, best_solution_length = [
        None for _ in range(len(distance_matrix))
    ], float("inf")

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

            # TODO: petla robiąca replica transition
        # TODO: zakonczenie petli ktora wykonuje sie k razy i zmienijszanie temperatury i koniec

    return best_solution, best_solution_length
