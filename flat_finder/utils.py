from random import normalvariate


def sample(base: float, plus_range: float):
    factor = None

    while factor is None or factor > 1:
        factor = abs(normalvariate(0, 0.5))

    return base + factor + plus_range