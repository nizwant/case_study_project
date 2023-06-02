from src.Code.pt_sa import pt_sa
from src.Parameters.problems import problems
from src.Parameters.problems import problems_size
from src.Parameters.best_known_solution import best_known_solution
from src.Parameters.creating_df_for_parameter import get_samples
import pandas as pd
import random


def iterate_over_all_problems(parameters):
    # guide how to iterate over all problems easily
    # and how to get the best known solution length
    results = []
    for name, distance_matrix in problems.items():
        solution, solution_length = pt_sa(distance_matrix, **parameters)
        optimal_solution_length = best_known_solution[name]
        worse_rate = optimal_solution_length / solution_length * 100 - 100
        # print(f"Problem: {name}")
        # print(
        #     f"Our solution length: {solution_length}, optimal solution length: {optimal_solution_length}"
        # )
        # print(
        #     f"Our solution is worse by {worse_rate}%"
        # )
        results.append([name, solution_length, worse_rate])
    df = pd.DataFrame(results, columns=["Problem", "Solution Length", "Worse Rate"])
    print(df)
    print(f"Average worse rate: {df['Worse Rate'].mean()}%")

def iterate_over_samples(parametrs):
    # guide how to iterate over samples
    # and how to get the best known solution length
    results = []
    samples = get_samples()
    for sample in samples:
        distance_matrix = problems[sample]
        solution, solution_length = pt_sa(distance_matrix, **parametrs)
        optimal_solution_length = best_known_solution[sample]
        worse_rate = optimal_solution_length / solution_length * 100 - 100
        results.append([sample, solution_length, worse_rate])
    df = pd.DataFrame(results, columns=["Problem", "Solution Length", "Worse Rate"])
    print(df)
    print(f"Average worse rate: {df['Worse Rate'].mean()}%")



