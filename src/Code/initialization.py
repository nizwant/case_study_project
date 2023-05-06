from numpy.random import beta


def initiate_temperatures(
    n: int, min: float, max: float, a: float = 1, b: float = 1
) -> list:
    """
    Returns a list of n temperatures between min and max,
    with a and b as parameters for the beta distribution.
    if a = b = 1, the temperatures are uniformly distributed between min and max.
    """
    return beta(a, b, n) * (max - min) + min
