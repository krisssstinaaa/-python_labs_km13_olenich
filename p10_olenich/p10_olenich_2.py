import numpy as np

years = np.arange(1900, 2020+1, 1)
print(years)
def leap_year(list):
    leap_year_list = []
    for i in list:
        if i % 400 == 0: leap_year_list.append(i)
        elif i % 100 == 0: pass
        elif i % 4 == 0: leap_year_list.append(i)
        else: pass
    return leap_year_list

def days_in_month(leap_year, n, y):
    if n == 2:
        if y in leap_year: print("There is 29 days in this month!")
        else: print("There is 28 days in this month!")
    elif n == 7: print("There is 31 days in this month!")
    elif n % 2 == 0: print("There is 30 days in this month!")
    else: print("There is 31 days in this month!")
n = input("Please, enter the number of month(n): ")
y = input("Please, enter the value of the year(y): ")
while n.isdigit() == False or int(n) <= 0 or int(n) > 12 : n = input("Invalid number of month input, please try again: ")
while y.isdigit() == False or int(y) < 1900 or int(y) >= 2020: y = input("Invalid year input, please try again: ")
days_in_month(leap_year(years), int(n), int(y))