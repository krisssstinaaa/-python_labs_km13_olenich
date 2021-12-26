import factorial
import exp_root
import logarithm

def check(x):
    try:
        float(x)
    except ValueError:
        return False
    return True

def main():
    print("Hello! We have 3 modules to offer you:\n")
    print("factorial", "exp_root", "logarithm", "Choose one!", sep = "\n", end = "\n")
    module = input("Please, choose the package: ")
    while module not in ("factorial", "exp_root", "logarithm"):
        module = input("Incorrect input, trey again: ")
    
    if module == "factorial":
        print("Great! You`ve chosen the factorial module!\n")
        print("The module factorial consists of 1 function, so you will use it.\n")
        print(factorial.fact.__doc__, "\n")
        n = input("Enter the number n: ")
        while check(n) == False:
            n = input("Incorrect input, trey again: ")
        n = int(n)
        print("The factorial of n is", factorial.fact(n))

    if module == "exp_root":
        print("Great! You`ve chosen the exp_root module!\n")
        print("We have 4 functions to offer you:\n")
        print(exp_root.exponentation.exp2.__name__, exp_root.exponentation.exp3.__name__, exp_root.root.root2.__name__, exp_root.root.root3.__name__, sep = "\n")
        function = input("Choose one, please: ")
        if function not in ("exp2", "exp3", "root2", "root3"):
            function = input("Incorrect input, trey again: ")

        if function == "exp2":
            print(exp_root.exponentation.exp2.__doc__, "\n")
            n = input("Enter the number n:")
            while check(n) == False:
                n = input("Incorrect input, trey again: ")
            n = int(n)
            print("The result is", exp_root.exponentation.exp2(n))
        if function == "exp3":
            print(exp_root.exponentation.exp3.__doc__, "\n")
            n = input("Enter the number n:")
            while check(n) == False:
                n = input("Incorrect input, trey again: ")
            n = int(n)
            print("The result is", exp_root.exponentation.exp3(n))
        if function == "root2":
            print(exp_root.root.root2.__doc__, "\n")
            n = input("Enter the number n:")
            while check(n) == False:
                n = input("Incorrect input, trey again: ")
            n = int(n)
            print("The result is", exp_root.root.root2(n))
        if function == "root3":
            print(exp_root.root.root3.__doc__, "\n")
            n = input("Enter the number n:")
            while check(n) == False:
                n = input("Incorrect input, trey again: ")
            n = int(n)
            print("The result is", exp_root.root.root3(n))

    if module == "logarithm":
        print("Great! You`ve chosen the logarithm module!\n")
        print("We have 3 functions to offer you:\n")
        print(logarithm.log.__name__, logarithm.ln.__name__, logarithm.lg.__name__, sep = "\n")
        function = input("Choose one, please: ")
        if function not in ("log", "ln", "lg"):
            function = input("Incorrect input, try again: ")

        if function == "log":
            print(logarithm.log.__doc__, "\n")
            a = input("Enter the number a: ")
            while check(a) == False:
                a = input("Incorrect input, try again: ")
            a = int(a)
            b = input("Enter the number b: ")
            while check(b) == False:
                b = input("Incorrect input, try again: ")
            b = int(b)
            print("The result is", logarithm.log(a, b))
        if function == "ln":
            print(logarithm.ln.__doc__, "\n")
            b = input("Enter the number b: ")
            while check(b) == False:
                b = input("Incorrect input, try again: ")
            b = int(b)
            print("The result is", logarithm.ln(b))
        if function == "lg":
            print(logarithm.lg.__doc__, "\n")
            b = input("Enter the number b:")
            while check(b) == False:
                b = input("Incorrect input, try again: ")
            b = int(b)
            print("The result is", logarithm.lg(b))

if __name__ == "__main__":
    while True:
        main()
        stop = input("1 - finish, any symbol - again: ")
        while check(stop) == False and (stop != "1" or stop != "0"):
            stop = input("Incorrect input, please try again: ")
        if stop == "1":
            print("Goodbye!")
            break
        else:
            continue
