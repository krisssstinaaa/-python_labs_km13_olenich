def root2(n: float) -> float:
    """
    The function returns a value of square root of the number n.\n
    n >= 0
    """
    if n < 0: 
        return "You`ve entered a negative number."
    else:
        return n**(1/2)

def root3(n: float) -> float:
    """
    The function returns a value of cube root of the number n.
    """
    if n < 0:
        return ((-1) * n)**(1/3)*(-1)
    if n >= 0:
        return n**(1/3)

