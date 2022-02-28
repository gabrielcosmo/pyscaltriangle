def fatorial(n):
    """
    Simple fatorial's calcule.
    :param n: number
    :return: int
    """
    c = n
    r = 1
    for x in range(0, c):
        r *= n
        n -= 1
    return r


def binomio(n, p):
    """
    Simple calcule of the Newton's Binomio.
    :param n: Number of elements
    :param p: Number of terms per set.
    :return: int
    """
    return fatorial(n) / (fatorial(p) * fatorial(n - p))
