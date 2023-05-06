from initialization import initialization


def pt_sa(
    distance_matrix: float,
    n: int,
    min_temperature: float,
    max_temperature: float,
    probability_of_shuffle: float,
    probability_of_heuristic: float,
    a: float,
    b: float,
) -> list:
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
