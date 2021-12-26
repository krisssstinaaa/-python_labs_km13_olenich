import math

def log(a, b) -> float:
    """
    The function returns a value of logarithm based on a for the number b.\n
    a != 1 and a > 0\n
    b > 0
    """
    if a == 1 or a <= 0 or b <= 0:
        return "You`ve entered 1, 0 or negative number."
    else:
        return math.log(b, a)

def ln(b) -> float:
    """
    The function returns a value of logarithm based on e for the number b.\n
    b > 0
    """
    return log(math.e, b)

def lg(b) -> float:
    """
    The function returns a value of logarithm based on 10 for the number b.\n
    b > 0
    """
    return log(10, b)

