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
    }

    solution, solution_length = pt_sa(distance_matrix, **parameters)
    print(f"Solution: {solution}\nSolution length: {solution_length}")


if __name__ == "__main__":
    main()
