a= float(input("Please enter the 'a' value:"))
b= float(input("Please enter the 'b' value:"))
c= float(input("Please enter the 'c' value:"))

discriminant_value= (b**2) - 4*a*c

if discriminant_value > 0:
  root_1= (-b+ discriminant_value**(0.5))/ (2*a)
  root_2= (-b- discriminant_value**(0.5))/ (2*a)

  print("There are 2 real roots and they are:", root_1, "and", root_2)

elif discriminant_value==0:
  root_1= -b/(2*a)

  print("There is one real root and it is:", root_1)

else:
  print("There are two complex roots")