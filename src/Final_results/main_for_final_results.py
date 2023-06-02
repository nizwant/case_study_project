import time

from src.Parameters.best_known_solution import best_known_solution
from src.Parameters.problems import problems

import pandas as pd
from pt_sa_for_results import pt_sa_for_results

def set_parameters(exec_time: float) -> dict:
    parameters = {
        "n": 20,  # 10
        "min_temperature": 0.1,
        "max_temperature": 50,
        "probability_of_shuffle": 0.1,  # 0.5
        "probability_of_heuristic": 0.7,  # 0.5
        "a": 1,  # 1
        "b": 1,  # 1
        "duration_of_execution_in_seconds": exec_time - 0.1,  # 60 * 4,
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
    exec_time = 60 * 5

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

        csv_filename = f"{filename_prefix}_{i+1}.csv"
        df.to_csv(csv_filename, index=False)

def main():
    ### results:
    #df = pd.DataFrame(columns=['best_solution_length', 'time'])
    #df = run_algorithm_for_results("br17")
    #solution, solution_length = pt_sa_for_results(problems["br17"], **set_parameters(10), df=df)
    #print(f"Last best solution: {solution}\nBest solution length: {solution_length}")
    #print(df)
    #df.to_csv("output_second_try.csv", index=False)

    ## for small
    #df = run_algorithm_for_results("ftv35")
    #print(df)
    #df.to_csv("sol_time_small.csv", index=False)

    #for medium
    #df = run_algorithm_for_results("ftv64")
    #print(df)
    #df.to_csv("sol_time_medium.csv", index=False)

    # for big
    # print(df)
    # df.to_csv("sol_time_big.csv", index=False)
    df_time_creating('ftv35',15)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
