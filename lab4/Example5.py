n= int(input("Please enter the number 'n': "))

factor= 1

for i in range(n):
  i+=1
  factor *= i

print(factor)

trailing_zeros=0
for z in reversed(str(factor)):
  if z!= "0":
    break
  trailing_zeros += 1

print("Number of trailing zeros are: ", trailing_zeros)