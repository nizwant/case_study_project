from initialization import initialization
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
) -> tuple[list[int], float]:
    start = time()
    best_solution, best_solution_length = [
        None for _ in range(len(distance_matrix))
    ], float("inf")

    temperatures, transition_function_types, initial_solutions = initialization(
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
        pass
    # TODO: petla w ktorej robi sie k razy
    # TODO: w niej petla (potencjalnie zwielowątkowiona) która dla kazdego stanu
    # TODO: robi metropolis transition sprawdza czy jest lepszy od najlepszego koniec petli
    # TODO: kolejna petla potem robi replica transition
    # TODO: zakonczenie petli ktora wykonuje sie k razy i zmienijszanie temperatury i powtarzamy
    # TODO: az do skonczenia czasu

    return best_solution, best_solution_length
