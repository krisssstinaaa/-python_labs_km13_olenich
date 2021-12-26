def fact(n: int) -> int:
    """
    The function returns a value of factorial of number n.\n
    n >= 0
    """
    if n < 0:
        raise ValueError("You`ve entered the negative number.") 
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial
