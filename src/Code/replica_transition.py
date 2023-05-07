from random import randrange, uniform


def replica_transition(
        swap_prob: float,
        temperatures: list[float],
        n: int
) -> list:
    """
    Perform replica transition on given states.
    swap_prob is probability of swapping states.
    """
    first_index = randrange(n)

    while True:
        second_index = randrange(n)
        if second_index != first_index:
            break

    if uniform(0, 1) < swap_prob:
        temperatures[first_index], temperatures[second_index] = temperatures[second_index], temperatures[first_index]

    return temperatures
