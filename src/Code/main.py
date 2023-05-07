from pt_sa import pt_sa


def main():
    # read from file
    distance_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # random parameters, do not take them as point of reference
    parameters = {
        "n": 10,
        "min_temperature": 0.1,
        "max_temperature": 100,
        "probability_of_shuffle": 0.5,
        "probability_of_heuristic": 0.5,
        "a": 1,
        "b": 1,
        "duration_of_execution_in_seconds": 60 * 4,
        "k": 10,
        "max_length_percent_of_cycle": 0.2,  # max 0.3 more will result in bugs
        "swap_prob": 0.1
    }

    solution, solution_length = pt_sa(distance_matrix, **parameters)
    print(f"Solution: {solution}\nSolution length: {solution_length}")


# TODO: handling cooling
# TODO: handling replica transition
# TODO: handling acceptance of new solution in metropolis
# TODO: testing and debugging
# TODO: profiling
# TODO: parameters

if __name__ == "__main__":
    main()
