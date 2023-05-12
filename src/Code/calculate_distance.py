def cycle_length(cycle: list, distances_matrix: list[list[float]]) -> float:
    """
    Calculates the length of a cycle taking into account that the cycle must
    return from the last city to the first city.

    :param cycle:
        A list of integers representing the order in which cities are visited.
        The first and last cities should be the same, i.e., cycle[0] == cycle[-1].
    :param distances_matrix:
        A square matrix of distances between cities. The element at index (i, j)
        represents the distance between city i and city j.

    :return:
        float: The total length of the cycle
    """
    assert len(cycle) == len(distances_matrix), "Cycle should visit all cities"
    length = 0
    for i in range(len(cycle) - 1):
        length += distances_matrix[cycle[i]][cycle[i + 1]]
    length += distances_matrix[cycle[-1]][cycle[0]]
    return length


# ?to delete possibly
# def path_length(path: list, distances_matrix: list[list[float]]) -> float:
#     """
#     Calculates the length of a path.

#     :param path:
#         A list of integers representing the order in which cities are visited.
#     :param distances_matrix:
#         A square matrix of distances between cities. The element at index (i, j)
#         represents the distance between city i and city j.

#     :return:
#         float: The total length of the path
#     """
#     length = 0
#     for i in range(len(path) - 1):
#         length += distances_matrix[path[i], path[i + 1]]
#     return length
