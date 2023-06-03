import time
from run_algorithm import run_for_one_problem, iterate_over_all_problems, iterate_over_all_problems_with_time


def main():
    # run_for_one_problem("rbg403")
    iterate_over_all_problems()


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
