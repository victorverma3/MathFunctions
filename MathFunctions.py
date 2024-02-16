from BasicMath import *
from LinearAlgebra import *
from StochasticProcesses import *


if __name__ == "__main__":
    # print(
    #     LinearAlgebra.solve_linear_system(
    #         left_side=np.array(
    #             [
    #                 [1, 0, 0, 0, 0, 0, 0],
    #                 [1 / 6, -5 / 6, 1 / 6, 1 / 6, 0, 1 / 6, 0],
    #                 [1 / 6, 1 / 6, -5 / 6, 0, 1 / 6, 0, 1 / 6],
    #                 [1 / 6, 1 / 6, 0, -5 / 6, 0, 1 / 6, 1 / 6],
    #                 [1 / 6, 0, 1 / 6, 0, -5 / 6, 1 / 6, 1 / 6],
    #                 [0, 1 / 6, 0, 1 / 6, 1 / 6, -5 / 6, 1 / 6],
    #                 [0, 0, 1 / 6, 1 / 6, 1 / 6, 1 / 6, -5 / 6],
    #             ]
    #         ),
    #         right_side=np.array([1, 0, 0, 0, 0, 0, 0]),
    #     )
    # )
    print(StochasticProcesses.gamblers_ruin_probability(p=0.49292929, N=100, k=50))
    print(StochasticProcesses.gamblers_ruin_probability(p=0.49292929, N=1000, k=500))
    print(StochasticProcesses.gamblers_ruin_probability(p=0.5029237, N=100, k=50))
    print(StochasticProcesses.gamblers_ruin_probability(p=0.5029237, N=1000, k=500))
