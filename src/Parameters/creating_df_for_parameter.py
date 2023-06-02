import pandas as pd
import random
from src.Code.pt_sa import pt_sa
from src.Parameters.problems import problems
from src.Parameters.problems import problems_size
from src.Parameters.best_known_solution import best_known_solution


def generate_dataframe(parameters: dict, values: list, parameter: str, distance_matrix: list[list[float]]) -> pd.DataFrame:
    result = []
    for value in values:
        parameters_copy = parameters.copy()
        parameters_copy[parameter] = value
        solution, solution_length = pt_sa(distance_matrix, **parameters_copy)
        result.append([value, solution_length])
    df = pd.DataFrame(result, columns=[parameter, "Solution Length"])
    return df

def generate_parametrs_summary(parameters: dict, parametrs_grid: dict) -> pd.DataFrame:
    result = []

    for parametr_name, parametr_values in parametrs_grid.items():
        for value in parametr_values:
            parameters_copy = parameters.copy()
            if len(parametr_values) == 1:
                continue
            parameters_copy[parametr_name] = value
            print(value)
            samples = get_samples()
            #samples = problems.keys() # all samples
            for sample in samples:
                distance_matrix = problems[sample]
                solution, solution_length = pt_sa(distance_matrix, **parameters_copy)
                optimal_solution_length = best_known_solution[sample]
                worse_rate = optimal_solution_length / solution_length * 100 - 100
                result.append([str(sample), str(solution_length), str(worse_rate), str(parametr_name)] + list(parameters_copy.values()))

            with open(f"results.csv", "w") as f:
                f.write(str(result))
    df = pd.DataFrame(result, columns=["Problem", "Solution Length", "Worse Rate", "Parametr changed"] + list(parameters.keys()))
    return df

def get_samples():
    small, medium, big = [], [], []
    while(True):
       small = random.choice(list(problems_size.keys()))
       if problems_size[small] < 50:
           break

    while(True):
        medium = random.choice(list(problems_size.keys()))
        if problems_size[medium] > 50 and problems_size[medium] < 100:
            break

    while(True):
        big = random.choice(list(problems_size.keys()))
        if problems_size[big] > 100:
            break

    return [small, medium, big]