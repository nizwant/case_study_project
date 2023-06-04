import threading


from src.Code.cooling import cooling
from src.Code.initialization import initialization
from src.Code.metropolis_transition import metropolis_transition
from src.Code.replica_transition import replica_transition

import pandas as pd

def update_state(
        solutions: list[list[int]],
        solutions_lengths: float,
        distance_matrix: list[list[float]],
        temperatures: list[float],
        max_temperature: float,
        transition_function_types: list[bool],
        max_length_percent_of_cycle: float,
        state: int,
        lock: threading.Lock,
):
    solution, solution_length = metropolis_transition(
        solutions[state],
        solutions_lengths[state],
        distance_matrix,
        temperatures[state],
        max_temperature,
        transition_function_types[state],
        max_length_percent_of_cycle,
    )
    with lock:
        solutions[state], solutions_lengths[state] = solution, solution_length

import time
def pt_sa_for_results(
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
        cooling_rate: float,
        df: pd.DataFrame,
        time_given: float
) -> tuple[list[int], float, pd.DataFrame, float]:
    """
    Performs a Parallel Tempering Simulated Annealing
    algorithm on a given distance matrix.
    """
    start = time.time()
    best_solution = [None for _ in range(n)]
    best_solution_length = float("inf")

    temperatures, transition_function_types, solutions, solutions_lengths = initialization(
        distance_matrix,
        n,
        min_temperature,
        max_temperature,
        probability_of_shuffle,
        probability_of_heuristic,
        a,
        b,
    )

    while time.time() - start < duration_of_execution_in_seconds:
        for _ in range(k):
            threads = []
            lock = threading.Lock()
            for state in range(n):
                thread = threading.Thread(
                    target=update_state,
                    args=(
                        solutions,
                        solutions_lengths,
                        distance_matrix,
                        temperatures,
                        max_temperature,
                        transition_function_types,
                        max_length_percent_of_cycle,
                        state,
                        lock,
                    ),
                )
                thread.start()
                threads.append(thread)
            for thread in threads:
                thread.join()

            for state in range(n):
                if solutions_lengths[state] < best_solution_length:
                    best_solution, best_solution_length = (
                        solutions[state],
                        solutions_lengths[state],
                    )

                    elapsed_time = time.time() - start + time_given

                    new_row = pd.DataFrame({'best_solution_length': [best_solution_length], 'time': [elapsed_time]})
                    df = pd.concat([df, new_row], ignore_index=True)

                    print(f"Best solution: {best_solution}\nBest solution length: {best_solution_length}")

            for _ in range(n):
                temperatures = replica_transition(
                    swap_states_probability,
                    closeness,
                    temperatures,
                    solutions_lengths,
                    best_solution_length,
                    n,
                )

        for state in range(n):
            temperatures[state] = cooling(
                cooling_rate, temperatures[state], min_temperature
            )

    return best_solution, best_solution_length, df, time_given + (time.time() - start)