integer_= int(input("Please enter an integer: "))
while integer_ < 0:
  integer_= int(input("Please enter a valid integer: "))

while integer_>10:
  integer_= int(input("Please enter an integer less than 10: "))


for i in range(10):
  i= int(i) + 1
  print( integer_ , "x", i, "=", i*integer_)

