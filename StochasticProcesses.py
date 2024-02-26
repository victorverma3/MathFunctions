from BasicMath import add, sub, mul, div, exp, factorial
import numpy as np


def gamblers_ruin_probability(p, N, k):
    """calculates the probability of ruin with winning probability p, target value N, and starting value k"""

    # verifies parameters
    if p < 0 or p > 1:
        raise ValueError("p must be between 0 and 1")
    if type(N) == int:
        if N < 1:
            raise ValueError("N must either be an integer greater than 0 or infinity")
    else:
        if N != "inf":
            raise ValueError("N must either be an integer greater than 0 or infinity")
    if type(k) != int or k < 0:
        raise ValueError("k must be an integer greater than or equal to 0")

    # calculations
    q = 1 - p

    if N == "inf":
        if 1 - p < p:
            return exp(div(q, p), k)
        else:
            return 1
    else:
        if p == 0.5:
            return sub(1, div(k, N))
        else:
            return sub(
                1,
                div(
                    sub(1, exp(div(q, p), k)),
                    sub(1, exp(div(q, p), N)),
                ),
            )


def gamblers_ruin_length(p, N, k):
    """calculates the expected time to ruin with winning probability p, target value N, and starting value k"""

    # verifies parameters
    if p < 0 or p > 1:
        raise ValueError("p must be between 0 and 1")
    if type(N) == int:
        if N < 1:
            raise ValueError("N must either be an integer greater than 0 or infinity")
    else:
        if N != "inf":
            raise ValueError("N must either be an integer greater than 0 or infinity")
    if type(k) != int or k < 0:
        raise ValueError("k must be an integer greater than or equal to 0")

    # calculations
    q = 1 - p

    if N == "inf":
        if p > 0.5:
            return "it does not make sense to ask this question"
        if p == 0.5:
            return "inf"
        else:
            return div(k, sub(1, mul(2, p)))
    else:
        if p == 0.5:
            return mul(k, sub(N, k))
        else:
            return add(
                div(
                    mul(sub(1, exp(div(q, p), k)), N),
                    mul(
                        sub(1, mul(2, p)),
                        sub(1, exp(div(q, p), N)),
                    ),
                ),
                div(k, sub(1, mul(2, p))),
            )


def branching_extinction_probability(distribution, n):
    """calculates the extinction probability of a branching process through time step n, given the gamma distribution and a starting population of 1"""

    # verifies parameters
    if type(n) != int or n < 0:
        raise ValueError("k must be an integer greater than or equal to 0")

    # calculations using dynamic programming
    def phi(distribution, s):
        if distribution["name"] == "poisson":
            l = distribution["lambda"]
            return np.exp(sub(mul(s, l), l))
        elif distribution["name"] == "geometric":
            p = distribution["p"]
            return div(1, sub(1, mul(s, sub(1, p))))
        elif distribution["name"] == "binomial":
            n, p = distribution["n"], distribution["p"]
            return exp(add(sub(1, p), mul(s, p)), n)
        else:
            raise ValueError("invalid distribution")

    u = [0] * (n + 1)
    u[0] = 0

    if distribution["name"] == "custom":
        for j in range(1, n + 1):
            u[j] = sum(
                mul(exp(u[j - 1], k), distribution["values"][k])
                for k in distribution["values"]
            )
    else:
        for j in range(1, n + 1):
            u[j] = phi(distribution, u[j - 1])

    return {time: prob for time, prob in enumerate(u)}
