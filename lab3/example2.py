num1= float(input("Please enter the first number:"))
num2= float(input("Please enter the second number:"))
num3= float(input("Please enter the third number:"))

if num1<=num2 and num1<=num3:
  min_value= num1

elif num2<=num1 and num2<=num3:
  min_value= num2

else:
  min_value= num3

print("The minimum value is", min_value)