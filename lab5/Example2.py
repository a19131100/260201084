n = int(input("How many numbers?: "))
count=0
even_count=0
for i in range(n):
  integer_=int(input("Please enter an integer: "))
  if integer_%2==0:
    even_count+=1
  
percentage= (even_count/n)*100
print("%", percentage)

