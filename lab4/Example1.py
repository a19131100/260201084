digits= input("Please enter the number: ")

if len(digits)==1:
  sum_=digits
else:
  digits= int(digits)
  first_num= digits % 10
  second_num= ((digits % 100) - first_num) // 10
  sum_= first_num + second_num

print(sum_)


""""
digits= int(input("Please enter the number: "))

last_two= digits % 100
sum_=0
for i in str(last_two):
  sum_ += int(i)

print(sum_)      #code for the for loop
"""







