
digits= int(input("Please enter the number: "))

last_two= digits % 100
sum_=0
for i in str(last_two):
  sum_ += int(i)

print(sum_)








