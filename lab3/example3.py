gpa_point= float(input("Please enter your GPA:"))
number_of_lectures= int(input("Please enter the number of lectures:"))

if gpa_point<2.0:
  if number_of_lectures<47:
    print("Not enough number of lectures and GPA!")
  else:
    print("Not enough GPA!")

else:
  if number_of_lectures<47:
    print("Not enough number of lectures!")

  else:
    print("GRADUATED!")