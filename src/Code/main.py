import time
import random
from pt_sa import pt_sa
from src.Code.read_input import read_input
from src.Parameters.creating_df_for_parameter import generate_dataframe, generate_parametrs_summary
from src.Parameters.iterate_over_all_problems import iterate_over_all_problems, iterate_over_samples
from src.Parameters.problems import problems, problems_size
import pandas as pd

def main():
    # read from file
    # distance_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    file_path = "../ftv38.atsp"
    distance_matrix = read_input(file_path)
    random.seed(42)

    # random parameters, do not take them as point of reference
    parameters = {
        "n": 20, #10
        "min_temperature": 0.1,
        "max_temperature": 50,
        "probability_of_shuffle": 0.1, #0.5
        "probability_of_heuristic": 0.7, #0.5
        "a": 1, #1
        "b": 1, #1
        "duration_of_execution_in_seconds": 5  ,  # 60 * 4,
        "k": 20, #10
        "max_length_percent_of_cycle": 0.3,  # max 0.3 more will result in bugs
        "swap_states_probability": 0.1,
        "closeness": 1.5,
        "cooling_rate": 0.95  # 0.1 probably too low; actually suggested above 0.9
    }


    #parametr_test(parameters)
    iterate_over_all_problems(parameters)
    #iterate_over_samples(parameters)
    #iterate_over_samples(parameters)

# TODO: make cooling cooler
# TODO: testing and debugging
# TODO: profiling
# TODO: parameters (testing, description)

def parametr_test(parameters):
    parameters_grid = {
        "n": [20], #the more the better
        "min_temperature": [0.1],
        "max_temperature": [100],
        "probability_of_shuffle": [0.1], # the less the better
        "probability_of_heuristic": [1], # the more the better
        "a": [3, 2, 1, 0.5],
        "b": [3, 2, 1,  0.5],
        "duration_of_execution_in_seconds": [5],  # 60 * 4,
        "k": [10], #the more the better
        "max_length_percent_of_cycle": [0.2, 0.3 ],  # max 0.3 more will result in bugs, more is better
        "swap_states_probability": [0.05, 0.1], # the less the better???
        "closeness": [1.5],
        "cooling_rate": [0.9, 0.98, 0.8, 0.7, 0.95]  # 0.1 probably too low; actually suggested above 0.9
    }
    df = generate_parametrs_summary(parameters, parameters_grid)
    df.to_csv("grid_search_6.csv", index=False)
    print(df)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
