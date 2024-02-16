import numpy as np


class LinearAlgebra:

    def solve_linear_system(left_side, right_side):
        """solves a system of linear equations"""

        return np.linalg.inv(left_side).dot(right_side)
