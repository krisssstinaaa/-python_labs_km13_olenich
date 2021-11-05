import numpy as np
import itertools

def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size=(dim, dim))
    return matrix

def permutations(n):
    """
    The function finds all of the permutations of matrix
    and add them to list.
    """
    per = ""
    for i in range(0, n):
        per += str(i)
    permutations = list(itertools.permutations(str(per), n))
    return permutations

def convert_pm(pms):
    """
    The function converts the array of strigs into the array of numbers.
    (str -> int)
    """
    pm = []
    for p in pms:
        px = []
        for x in p:
            px.append(int(x))
        pm.append(px)
    return pm

def inversions(pm, n):
    """
    The function calculates the number of inversions in permutations of
    the matrix.
    """
    m = 0
    for i in range(0, n):
        el = pm[i]
        for x in range(i, n):
            if el > pm[x]:
                m += 1
    return m

def multiply(matrix, elements):
    """
    The function multiply the elements of the matrix.
    """
    res = 1
    i = 0
    for element in elements:
        res *= matrix[element][i]
        i += 1
    return res

def find_sum(matrix, perms, n):
    """
    The function finds sum all of the combinations.
    """
    res = 0
    for pm in perms:
        sign = 0
        if inversions(pm, n) % 2 == 0:
            sign = 1
        else:
            sign = -1
        res += sign * multiply(matrix, pm)
    return res

if __name__ == '__main__':
    mdim = 0
    while True:
        matrix_dim = input()
        try:
            mdim = int(matrix_dim)
        except:
            print("Abnormal value")
            continue
        if mdim > 10 or mdim <= 0:
            print("Abnormal value")
            continue
        break
    pms = permutations(mdim)
    matrix = random_matrix(mdim)

    print("Here is your matrix:", matrix)
    print("Here is the determinant of your matrix:", find_sum(matrix, convert_pm(pms), mdim))