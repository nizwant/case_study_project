def read_input(file_path: str) -> list[list[float]]:
    """
    Reads distance matrix from input file.
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # find dimension from the line that contains "DIMENSION:"
    dimension_line = next(line for line in lines if "DIMENSION:" in line)
    dimension = int(dimension_line.split(":")[1].strip())

    # skip the first 7 lines and any whitespace characters
    start_index = 7
    while lines[start_index].isspace():
        start_index += 1

    # skip the last line
    end_index = len(lines) - 1

    # create a matrix from the remaining lines
    distances = []
    for i in range(start_index, end_index):
        row = lines[i].split()
        if len(distances) == 0:
            distances.append([int(x) for x in row])
        elif len(distances[-1]) == dimension:
            distances.append([int(x) for x in row])
        else:
            k = dimension - len(distances[-1])
            distances[-1].extend([int(x) for x in row[:k]])
            if len(row) > k:
                distances.append([int(x) for x in row[k:]])
    return distances
