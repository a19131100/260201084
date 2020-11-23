numofstudents= int(input("How many students are there?: "))
list_of_students= []

for i in range(numofstudents):
  midterm1= int(input("Enter the first midterm grade: "))
  midterm2= int(input("Enter the second midterm grade: "))
  final= int(input("Enter final grade: "))
  list_of_students.append([midterm1, midterm2, final])

avg_grades= []
avg_=0
for grade in list_of_students:
  avg_ = grade[0] * (0.3) + grade[1] * (0.3) + grade[2] * (0.4)
  avg_grades.append(avg_)

print("All students average grades are: ", avg_grades)


