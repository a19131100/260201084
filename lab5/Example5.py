
fibo= int(input("How many fibonacci numbers do you want to see?: "))
a=1
b=0

for i in range(fibo):
  sums=a+b
  b=a
  a=sums
  print(b)





