integer1= int(input("Please enter the first number: "))
integer2= int(input("Please enter the second number: "))

common_count=0

while integer1 > 0 and integer2> 0:
  if integer1%10 == integer2%10:
    common_count+=1
  
  integer1= integer1//10
  integer2= integer2//10
  

print("Match:", common_count)
  



  

