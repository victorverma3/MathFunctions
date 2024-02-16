from BasicMath import *


class StochasticProcesses:
    def gamblers_ruin(p, N, k):
        if p < 0 or p > 1:
            raise ValueError("p must be between 0 and 1")
        if type(N) == int:
            if N < 1:
                raise ValueError(
                    "N must either be an integer greater than 0 or infinity"
                )
        else:
            if N != "inf":
                raise ValueError(
                    "N must either be an integer greater than 0 or infinity"
                )
        if type(k) != int or k < 0:
            raise ValueError("k must be an integer greater than or equal to 0")

        q = 1 - p

        if N == "inf":
            if 1 - p < p:
                return BasicMath.exp(BasicMath.div(q, p), k)
            else:
                return 1

        else:
            if p == 0.5:
                return BasicMath.sub(1, BasicMath.div(k, N))
            else:
                return BasicMath.sub(
                    1,
                    BasicMath.div(
                        BasicMath.sub(1, BasicMath.exp(BasicMath.div(q, p), k)),
                        BasicMath.sub(1, BasicMath.exp(BasicMath.div(q, p), N)),
                    ),
                )
