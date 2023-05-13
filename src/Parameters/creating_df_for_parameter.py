import pandas as pd
import src.Code.pt_sa

def generate_dataframe(parameters: dict, values: list, parameter: str) -> pd.DataFrame:
    result = []
    for value in values:
        parameters_copy = parameters.copy()
        parameters_copy[parameter] = value
        solution, solution_length = src.pt_sa(**parameters_copy)
        result.append([value, solution_length])
    df = pd.DataFrame(result, columns=[parameter, "Solution Length"])
    return df



