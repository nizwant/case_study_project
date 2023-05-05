import numpy as np

name = "ftv38.atsp"


def parse(file_path):
    with open(file_path, "r") as f:
        # read the file line by line
        data = f.read().split()
        size = int(data[data.index("DIMENSION:") + 1])
        martix = np.array(
            data[data.index("EDGE_WEIGHT_SECTION") + 1 : -1], dtype=np.int32
        )
    return martix.reshape(size, size)


# print(parse(name))
# print(len(parse(name)))
