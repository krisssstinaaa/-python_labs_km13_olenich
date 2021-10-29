import math

print("Enter a, b and c: ")
print("ax^2 + bx + c = 0:")
a = input("a = ")
b = input("b = ")
c = input("c = ")

discr = b**2 - 4*a*c

try:
    if discr > 0:
        print("Discriminant D = %.2f" % discr)
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
    else:
        raise ValueError("There is no roots!")
except ZeroDivisionError as z:
    print(z)
    print("Raised when the second argument of a division or modulo operation is zero. The associated value is a string indicating the type of the operands and the operation.")
except OverflowError as o:
    print(o)
    print("Raised when the result of an arithmetic operation is too large to be represented.")
except TypeError as t:
    print(t)
    print("TypeError is raised whenever an operation is performed on an incorrect/unsupported object type.")
except Exception:
    print("Oops, something went wrong!")