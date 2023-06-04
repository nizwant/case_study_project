import threading
import warnings
from time import time

import pandas as pd

from src.Code.cooling import cooling
from src.Code.initialization import initialization
from src.Code.pt_sa import update_state
from src.Code.replica_transition import replica_transition
from src.Parameters.best_known_solution import best_known_solution
from src.Parameters.problems import problems


def pt_sa_test(
        distance_matrix: list[list[float]],
        df: pd.DataFrame,
        name: str,
        n: int,
        min_temperature: float,
        max_temperature: float,
        probability_of_shuffle: float,
        probability_of_heuristic: float,
        a: float,
        b: float,
        duration_of_execution_in_seconds: int,
        k: int,
        max_length_percent_of_cycle: float,
        swap_states_probability: float,
        closeness: float,
        cooling_rate: float,
        minutes: list[float],
        per_above_min: list[float]
) -> tuple[list[int], float, pd.DataFrame]:
    """
    Performs a Parallel Tempering Simulated Annealing
    algorithm on a given distance matrix.
    """
    start = time()
    best_solution = [None for _ in range(len(distance_matrix))]
    best_solution_length = float("inf")
    best_known_sol = df.loc[df['Name'] == name, 'best_known_sol'].iloc[0]

    temperatures, transition_function_types, solutions, solutions_lengths = initialization(
        distance_matrix,
        n,
        min_temperature,
        max_temperature,
        probability_of_shuffle,
        probability_of_heuristic,
        a,
        b,
    )

    iter_counter = 0
    while time() - start < duration_of_execution_in_seconds:
        iter_counter += 1
        for _ in range(k):
            threads = []
            lock = threading.Lock()
            for state in range(n):
                thread = threading.Thread(target=update_state, args=(
                    solutions,
                    solutions_lengths,
                    distance_matrix,
                    temperatures,
                    max_temperature,
                    transition_function_types,
                    max_length_percent_of_cycle,
                    state,
                    lock,
                ))
                thread.start()
                threads.append(thread)
            for thread in threads:
                thread.join()

            for state in range(n):
                if solutions_lengths[state] < best_solution_length:
                    best_solution, best_solution_length = solutions[state], solutions_lengths[state]

                    "calculating percent above best solution and if needed returns result"

                    above_best_sol = ((best_solution_length - best_known_sol) / best_known_sol) * 100
                    for percent in per_above_min:
                        if (above_best_sol <= percent) and (df.loc[df['Name'] == name, f'{percent}_%'].iloc[0] is None):
                            df.loc[df['Name'] == name, f'{percent}_%'] = time() - start
            for _ in range(n):
                temperatures = replica_transition(swap_states_probability,
                                                  closeness,
                                                  temperatures,
                                                  solutions_lengths,
                                                  best_solution_length,
                                                  n)

            # recording solution after certain time
            for minute in minutes:
                if time() - start > minute * 60 and (df.loc[(df['Name'] == name), f'{minute}_min'].iloc[0] is None):
                    df.loc[(df['Name'] == name), f'{minute}_min'] = best_solution_length

        for state in range(n):
            temperatures[state] = cooling(cooling_rate, temperatures[state], min_temperature)

    return best_solution, best_solution_length, df


def dataframe_test(minutes, closeness):
    df = pd.DataFrame(columns=["Name", "best_known_sol"])
    for name, length in best_known_solution.items():
        df = pd.concat([df, pd.DataFrame.from_records([{"Name": name, "best_known_sol": length}])], ignore_index=True)

    # testing solution after number of minutes
    for i in minutes:
        df[f'{i}_min'] = pd.Series([None] * len(df))

    # testing how long does it take to reach a certain closeness
    for i in closeness:
        df[f'{i}_%'] = pd.Series([None] * len(df))

    return df


def main():
    # Ignore the RuntimeWarning
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    minutes = [3, 2.5, 2, 1.5, 1, 0.5, 0.25]
    closeness = [50, 30, 20, 15, 10, 5, 3, 2, 1]
    df = dataframe_test(minutes, closeness)
    name = 'ftv33'
    num = 5
    # df.loc[df["Name"] == name, f"{num}_min"] = 3
    # print(df)
    # print(df.loc[(df['Name'] == name), f'{num}_min'] is None)
    # print(df.loc[df['Name'] == name, 'best_known_sol'].iloc[0])
    # print(problems[name])
    parameters = {
        "n": 20,  # 10
        "min_temperature": 0.1,
        "max_temperature": 50,
        "probability_of_shuffle": 0.1,  # 0.5
        "probability_of_heuristic": 0.7,  # 0.5
        "a": 1,  # 1
        "b": 1,  # 1
        "duration_of_execution_in_seconds": 186,  # 60 * 4,
        "k": 20,  # 10
        "max_length_percent_of_cycle": 0.3,  # max 0.3 more will result in bugs
        "swap_states_probability": 0.1,
        "closeness": 1.5,
        "cooling_rate": 0.95,  # 0.1 probably too low; actually suggested above 0.9
        "minutes": minutes,
        "per_above_min": closeness,
    }
    for name, length in best_known_solution.items():
        if name in problems:
            print(name)
            best_solution, best_solution_length, df = pt_sa_test(problems[name], df, name, **parameters)
    df.to_csv("dataframe")
    print(df)


if __name__ == '__main__':
    main()
