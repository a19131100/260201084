employees={}

for i in range(5):
  names= input("Name of the employee?: ")
  salaries= int(input("Salary of this employee?: "))
  employees[names]= salaries

print(employees)

sorted_salary_list= sorted(employees.values())
names_list= list(employees.keys())


print(max_three_salary)


