# import os
# from Code.read_input import read_input

# # assign directory
# directory = "/Users/mat/Desktop/untitled folder"

# # iterate over files in
# # that directory
# ff = open("/Users/mat/Desktop/wb/Warsztaty_Badawcze/src/Parameters/problems.txt", "w")
# ff.write("problems = {")

# for filename in os.listdir(directory):
#     f = os.path.join(directory, filename)
#     ff.write(f'"{filename.split(".")[0]}":{read_input(f)},')
# ff.write("}")
# ff.close()

from Parameters.problems import problems

for problem in problems:
    print(problem)
    print(problems[problem][0])
    print()
    break