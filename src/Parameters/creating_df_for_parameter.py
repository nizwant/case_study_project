import pandas as pd
from src.Code.pt_sa import pt_sa
from problems import problems
from best_known_solution import best_known_solution


def generate_dataframe(parameters: dict, values: list, parameter: str) -> pd.DataFrame:
    result = []
    for value in values:
        parameters_copy = parameters.copy()
        parameters_copy[parameter] = value
        solution, solution_length = pt_sa(**parameters_copy)
        result.append([value, solution_length])
    df = pd.DataFrame(result, columns=[parameter, "Solution Length"])
    return df


def iterate_over_all_problems(parameters):
    # guide how to iterate over all problems easily
    # and how to get the best known solution length
    for name, distance_matrix in problems.items():
        solution, solution_length = pt_sa(distance_matrix, **parameters)
        optimal_solution_length = best_known_solution[name]
        print(f"Problem: {name}")
        print(
            f"Our solution length: {solution_length}, optimal solution length: {optimal_solution_length}"
        )
        print(
            f"Our solution is worse by {optimal_solution_length / solution_length * 100 - 100}%"
        )
