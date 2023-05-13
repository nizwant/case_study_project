from src.Code.pt_sa import pt_sa
from problems import problems
from best_known_solution import best_known_solution


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
