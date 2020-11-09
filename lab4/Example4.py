a= int(input("Please enter the first number: "))
b= int(input("Please enter the second number: "))
mult=1

if a==0 and b==0:
  print("It cannot be calculated")

elif b<0:
  b=-b
  for i in range(b):
    mult *= a
  mult= 1/mult
  print(mult)

else:
  for i in range(b):
    mult *= a
  print(mult)
