salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
new_salary_list = list(map(lambda i: round(i * 1.3, 2), salary_list))
difference = list(map(lambda x, y: round(x - y, 2), new_salary_list, salary_list))
salary_table = [str([salary_list[i], new_salary_list[i], difference[i]]) for i in range(len(salary_list))]
print("Salary table:", *[i.replace("'", "").replace("[", "").replace("]", "").replace(",", "") for i in salary_table], sep = "\n")
