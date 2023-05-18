import time

from pt_sa import pt_sa
from src.Parameters.best_known_solution import best_known_solution
from src.Parameters.problems import problems


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


def iterate_over_all_problems():
    for name in problems.keys():
        solution, solution_length = run_algorithm(name)
        optimal_solution_length = best_known_solution[name]
        print(f"Problem: {name}")
        print(
            f"Our solution length: {solution_length}, optimal solution length: {optimal_solution_length}"
        )
        print(
            f"Our solution is worse by {optimal_solution_length / solution_length * 100 - 100}%"
        )


def run_for_one_problem(name: str):
    solution, solution_length = run_algorithm(name)
    print(f"Best solution: {solution}\nBest solution length: {solution_length}")


def main():
    iterate_over_all_problems()

    # parameters_test
    # TODO: should it be here?
    # values = [0.1, 0.2, 0.3, 0.4, 0.5]
    # df = generate_dataframe(parameters, values, "min_temperature", distance_matrix)
    # print(df.head())


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
