import time

from pt_sa import pt_sa
from src.Code.read_input import read_input
from src.Parameters.creating_df_for_parameter import generate_dataframe
import pandas as pd
def main():
    # read from file
    # distance_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    file_path = "../ftv38.atsp"
    distance_matrix = read_input(file_path)

    # random parameters, do not take them as point of reference
    parameters = {
        "n": 10,
        "min_temperature": 0.1,
        "max_temperature": 100,
        "probability_of_shuffle": 0.5,
        "probability_of_heuristic": 0.5,
        "a": 1,
        "b": 1,
        "duration_of_execution_in_seconds": 5,  # 60 * 4,
        "k": 10,
        "max_length_percent_of_cycle": 0.2,  # max 0.3 more will result in bugs
        "swap_states_probability": 0.1,
        "closeness": 1.5,
        "cooling_rate": 0.1  # probably too low; actually suggested above 0.9
    }

    solution, solution_length = pt_sa(distance_matrix, **parameters)
    print(f"Solution: {solution}\nSolution length: {solution_length}")

### parameters_test
    values = [0.1,0.2,0.3,0.4,0.5]
    df = generate_dataframe(parameters, values, 'min_temperature', distance_matrix)
    print(df.head())

# TODO: make cooling cooler
# TODO: testing and debugging
# TODO: profiling
# TODO: parameters (testing, description)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
