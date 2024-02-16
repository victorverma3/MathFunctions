class BasicMath:
    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def mul(x, y):
        return x * y

    def div(dividend, divisor, variant="f"):
        if divisor == 0:
            raise ValueError("divide by 0")

        if variant not in ["f", "i"]:
            raise ValueError("variant must be f or i")

        if variant == "f":
            quotient = dividend / divisor
        else:
            quotient = dividend // divisor

        return quotient

    def exp(base, power):
        return base**power
