import pandas as pd
from src.Code.pt_sa import pt_sa


def generate_dataframe(parameters: dict, values: list, parameter: str, distance_matrix: list[list[float]]) -> pd.DataFrame:
    result = []
    for value in values:
        parameters_copy = parameters.copy()
        parameters_copy[parameter] = value
        solution, solution_length = pt_sa(distance_matrix,**parameters_copy)
        result.append([value, solution_length])
    df = pd.DataFrame(result, columns=[parameter, "Solution Length"])
    return df
