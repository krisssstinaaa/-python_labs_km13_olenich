#This program is used for calculating employees' new salary.
salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
new_salary_list = [i*1.3 for i in salary_list] # The cycle "for" in lines 3 and 4 is used for avoiding initalizing a new variable for every element of the list
new_salary_list_rounded = [round(k,2) for k in new_salary_list]
print("Salary Table:")
print(*salary_list, sep=", ")
print(*new_salary_list_rounded, sep=", ")
