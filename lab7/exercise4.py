employees={}

for i in range(5):
  names= input("Name of the employee?: ")
  salaries= int(input("Salary of this employee?: "))
  employees[names]= salaries

employee_list = sorted(employees, key=employees.get, reverse=True)[:3]

print(employee_list)


