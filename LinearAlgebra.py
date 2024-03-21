import numpy as np


def solve_linear_system(left_side, right_side):
    """solves a system of linear equations"""

    return np.linalg.solve(left_side, right_side)
