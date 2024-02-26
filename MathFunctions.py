from BasicMath import *
from LinearAlgebra import *
from StochasticProcesses import *


if __name__ == "__main__":
    print(
        branching_extinction_probability(
            {"name": "custom", "values": {0: 0.5, 2: 0.5}}, 5
        )
    )
    print(branching_extinction_probability({"name": "poisson", "lambda": 1.1}, 5))
