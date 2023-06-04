# Warsztaty_Badawcze

This repository contains a project that aims to solve the Asymmetric Traveling Salesman Problem (ATSP) using a combination of simulated annealing and parallel tempering algorithms.
The TSP is a well-known combinatorial optimization problem that asks for the shortest route a salesman can take to visit a set of cities exactly once and return to the starting city. In the asymmetric variant, the distance between two cities may differ depending on the direction traveled.

Main case study repository: https://github.com/PrzeChoj/2023Lato-WarsztatyBadawcze <br />
Data we used to test our algorithm: http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/atsp/ <br />
Known best solutions to these problems: http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/ATSP.html

## Team members
- Marta Szuwarska ([@szuvarska](https://github.com/szuvarska))
- Karolina Mączka ([@KarolinaMaczka](https://github.com/KarolinaMaczka))
- Magdalena Jeczeń ([@m24jeczen](https://github.com/m24jeczen))
- Łukasz Grabarski ([@LukaszGrabarski](https://github.com/LukaszGrabarski))
- Mateusz Nizwantowski ([@nizwant](https://github.com/nizwant))

## Function execution guide

This guide provides instructions on how to execute the functions included in this repository. 

After cloning the repository, please go to the script `src/main.py`. There are imported three main functions to use.

### Solving one problem
If you want to run the algorithm for one specific problem (multiple runs during 5 minutes period), use the function `run_for_one_problem(problem_name)` provided with string name of the problem as a parameter. All the available problems are stored in a dictionary here `src/Parameters/problems.py`. If you want to test our algorithm for a new problem, add it to the dictionary along with a given distance matrix. 

### Iterating over all problems
If you want to run the algorithm for all provided problems (multiple runs during 5 minutes period), use the function `iterate_over_all_problems()`. The results will be stored here: `src/Tests/Results` in a file called `My_results.csv`.

### Iterating over all problems with given time
If you want to run the algorithm for all provided problems with one run per problem of given time, use the function `iterate_over_all_problems_with_time(exec_time)` provided with time in seconds as parameter. The results will be stored here: `src/Tests/Results` in a file called `long_term_results.csv`.

## Directory guide

### Structure

```bash
.
├── .gitignore
├── requirements.txt
├── README.md
└── src
    ├── main.py
    ├── Code
    │   ├── calculate_distance.py
    │   ├── cooling.py
    │   ├── initialization.py
    │   ├── metropolis_transition.py
    │   ├── pt_sa.py
    │   ├── read_input.py
    │   ├── replica_transition.py
    │   └── run_algorithm.py
    ├── Cython
    ├── Final_results
    ├── Parameters
    │   └── results
    └── Tests
        ├── Cython_tests
        ├── Heuristic_tests
        ├── Long_term_tests
        ├── Monkey_test
        ├── Results
        └── Time_tests
```
### Description of directories

- Code - directory with all the code needed to run the functions in `src/main.py`
- Cython - directory with all the code from Code but compiled in C language using Cython, script for compilation called `setup.py` and equivalent of `main.py`.
- Final_results - all files with final results of algorithm, scripts for those tests and scripts for plots of the results.
- Parameters - all files with results of testing parameters, scripts for those tests and scripts for plots of the results.
- Tests - results of additional tests (Cython, heuristic on its own, long term tests etc.) and scripts for plots of the results.

## The Race

- first task: ftv38 \
Our solution: [14, 17, 18, 19, 1, 15, 6, 7, 5, 8, 37, 9, 10, 11, 12, 13, 36, 20, 21, 22, 23, 24, 25, 26, 31, 32, 33, 29, 28, 27, 30, 34, 38, 35, 4, 2, 3, 0, 16] \
Length of our solution: 1608 

- second task: ft70 \
Our solution: [40, 36, 42, 41, 37, 69, 65, 68, 67, 63, 66, 64, 48, 43, 49, 47, 55, 51, 50, 18, 30, 15, 7, 13, 14, 12, 10, 9, 5, 3, 60, 59, 57, 44, 46, 45, 58, 27, 22, 21, 26, 6, 0, 1, 2, 4, 23, 52, 54, 53, 20, 17, 16, 19, 25, 11, 8, 34, 32, 29, 24, 56, 33, 31, 62, 61, 28, 35, 38, 39] \
Length of our solution: 40218 

- third task: rbg403 \
Our solution: [100, 227, 141, 23, 14, 62, 13, 205, 289, 65, 248, 366, 292, 343, 33, 376, 68, 90, 72, 224, 388, 42, 287, 83, 43, 34, 295, 169, 308, 394, 129, 58, 8, 344, 64, 3, 2, 61, 107, 386, 47, 112, 322, 395, 103, 260, 5, 387, 9, 84, 272, 28, 314, 75, 10, 55, 367, 59, 310, 29, 24, 97, 259, 106, 165, 78, 226, 258, 79, 69, 245, 81, 22, 21, 82, 247, 212, 183, 397, 153, 20, 101, 164, 15, 131, 267, 46, 85, 67, 66, 60, 44, 88, 96, 338, 194, 86, 334, 160, 365, 231, 92, 51, 49, 37, 249, 256, 120, 392, 351, 293, 167, 221, 150, 151, 369, 187, 179, 303, 57, 242, 70, 349, 400, 99, 389, 180, 359, 206, 30, 373, 355, 6, 127, 48, 196, 345, 130, 193, 230, 382, 320, 254, 223, 168, 182, 91, 278, 122, 119, 309, 93, 203, 384, 383, 197, 146, 381, 105, 391, 154, 111, 340, 265, 311, 157, 339, 236, 108, 255, 54, 109, 275, 210, 110, 326, 325, 207, 45, 363, 204, 123, 192, 94, 170, 284, 329, 294, 257, 162, 133, 269, 181, 174, 185, 175, 332, 173, 305, 215, 115, 114, 241, 333, 238, 128, 228, 198, 402, 264, 274, 176, 190, 156, 390, 374, 393, 316, 12, 132, 243, 288, 291, 315, 161, 148, 147, 134, 306, 73, 152, 143, 188, 276, 125, 74, 214, 401, 216, 200, 297, 331, 323, 354, 342, 266, 95, 304, 218, 159, 76, 222, 136, 195, 237, 217, 300, 251, 113, 138, 18, 171, 296, 298, 63, 377, 50, 229, 225, 239, 346, 307, 271, 317, 313, 7, 286, 273, 350, 137, 36, 201, 268, 135, 280, 279, 385, 199, 348, 290, 202, 189, 208, 158, 277, 246, 142, 163, 25, 0, 220, 299, 233, 149, 347, 341, 360, 52, 40, 39, 252, 399, 337, 240, 219, 357, 358, 235, 121, 98, 213, 17, 211, 330, 302, 178, 124, 1, 172, 26, 77, 31, 319, 335, 155, 378, 398, 396, 324, 144, 177, 250, 209, 364, 368, 262, 38, 270, 19, 71, 375, 191, 361, 16, 301, 379, 166, 80, 372, 41, 87, 56, 356, 328, 281, 186, 53, 102, 35, 104, 145, 139, 371, 370, 234, 318, 118, 285, 4, 283, 253, 232, 89, 11, 116, 244, 117, 353, 352, 140, 263, 336, 321, 362, 184, 282, 327, 126, 27, 312, 261, 32, 380] \
Length of our solution: 2957 
