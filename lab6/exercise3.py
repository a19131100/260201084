numofstudents= int(input("How many students are there?: "))
list_of_students= []

for i in range(numofstudents):
  midterm1= int(input("Enter the first midterm grade: "))
  midterm2= int(input("Enter the second midterm grade: "))
  final= int(input("Enter final grade: "))
  list_of_students.append([midterm1, midterm2, final])

a_grades=[]
avg_=0
for grade in list_of_students:
  avg_ = grade[0] * (0.3) + grade[1] * (0.3) + grade[2] * (0.4)
  if avg_ > 90:
    a_grades.append(avg_)


if len(a_grades)>0:
  print("All AA average grades are: ", a_grades)

else:
  print("There is no AA student")