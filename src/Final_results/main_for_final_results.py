import time

from src.Parameters.best_known_solution import best_known_solution
from src.Parameters.problems import problems

import pandas as pd
from pt_sa_for_results import pt_sa_for_results

from src.Code.pt_sa import pt_sa

def set_parameters(exec_time: float) -> dict:
    parameters = {
        "n": 20,  # 10
        "min_temperature": 0.1,
        "max_temperature": 50,
        "probability_of_shuffle": 0.1,  # 0.5
        "probability_of_heuristic": 0.7,  # 0.5
        "a": 1,  # 1
        "b": 1,  # 1
        "duration_of_execution_in_seconds": exec_time - 30,  # 60 * 4,
        "k": 20,  # 10
        "max_length_percent_of_cycle": 0.3,  # max 0.3 more will result in bugs
        "swap_states_probability": 0.1,
        "closeness": 1.5,
        "cooling_rate": 0.95,  # 0.1 probably too low; actually suggested above 0.9
    }
    return parameters

def run_algorithm_for_results(problem_name: str) -> pd.DataFrame:
    distance_matrix = problems[problem_name]
    N = len(distance_matrix)
    exec_time = 5*60

    if N < 300:
        num_of_runs = int(exec_time / 30)
        parameters = set_parameters(30)
    else:
        num_of_runs = int(exec_time / 150)
        parameters = set_parameters(150)

    dff = pd.DataFrame(columns=['best_solution_length', 'time'])
    best_solution, best_solution_length, dff, timme = pt_sa_for_results(distance_matrix, **parameters, df =dff, time_given=0)

    for _ in range(num_of_runs):
        best_solution, best_solution_length, dff, timme = pt_sa_for_results(distance_matrix, **parameters, df=dff, time_given= timme)

    return dff

def df_time_creating(filename_prefix, num_iterations):
    for i in range(num_iterations):
        df = run_algorithm_for_results(filename_prefix)

        csv_filename = f"{filename_prefix}_{i+2}.csv"
        df.to_csv(csv_filename, index=False)

def iterate_over_all_problems_2():
    data = []

    for problem_name, distance_matrix in problems.items():
        best_solution, best_solution_length = run_algorithm(problem_name)
        optimal_solution_length = best_known_solution[problem_name]

        data.append({
            'our_solution_length': best_solution_length,
            'optimal_solution_length': optimal_solution_length
        })

    df = pd.DataFrame(data)
    return df

def run_algorithm(problem_name: str):
    distance_matrix = problems[problem_name]
    N = len(distance_matrix)
    exec_time = 60 * 5
    if N < 300:
        num_of_runs = int(exec_time / 30)
        parameters = set_parameters(30)
    else:
        num_of_runs = int(exec_time / 150)
        parameters = set_parameters(150)
    best_solution = [None for _ in range(len(distance_matrix))]
    best_solution_length = float("inf")
    for _ in range(num_of_runs):
        solution, solution_length = pt_sa(distance_matrix, **parameters)
        if solution_length < best_solution_length:
            best_solution, best_solution_length = solution, solution_length
    return best_solution, best_solution_length

def main():
    #df_time_creating('ftv35',15)
    #df_time_creating('ft70', 15)
    #df = iterate_over_all_problems_2()
    #df.to_csv("all_problems_results_2.csv", index=False)
    #df = iterate_over_all_problems_2()
    #df.to_csv("all_problems_results_3.csv", index=False)
    #df = iterate_over_all_problems_2()
    #df.to_csv("all_problems_results_4.csv", index=False)
    df_time_creating('rbg358', 14)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
