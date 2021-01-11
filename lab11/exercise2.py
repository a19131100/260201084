class Employee:
  
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  def get_name(self):
    return self.name

  def set_name(self):
    if name != "":
      self.name = name

  def get_salary(self):
    return self.salary

  def set_salary(self):
    if salary > 0:
      self.salary = salary

  def display(self):
    print("Name:", str(self.name))
    print("Salary:", str(self.salary))


class Company:

  def __init__(self, employee_list):
    self.employee_list = []

  def get_employee_list(self):
    return self.employee_list

  def set_employee_list(self, current_list):
    if type(current_list) == list:
      self.employee_list = current_list

  def add_employee(self, new_employee):
    if isinstance(new_employee, Employee):
      self.employee_list.append(new_employee)

  def calc_avg_salary(self):
    total_sum = 0
    for employee in self.employee_list:
      total_sum += emp.get_salary()

    return total_sum / len(self.employee_list)

  def display(self):
    for emp in self.employee_list:
      print("Name:", emp.get_name())
      print("Salary:", emp.get_salary())



c = Company()

e1 = Employee("Cem", 4000)
e2 = Employee("Merve", 4000)
e3 = Employee("Gamze", 4000)

c.add_employee(new_employee = e1)
c.add_employee(new_employee = e2)
c.add_employee(new_employee = e3)

c.display()
  
