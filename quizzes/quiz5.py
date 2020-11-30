name_= input("Please enter your name: ")
name_=name_.upper()

for letter in name_:
  print(letter)

stringconc= " "
anystr = input("Please enter any string ('quit' to quit): ")

while anystr!= "quit" :
  
  stringconc = stringconc + anystr
  
  anystr = input("Please enter any string ('quit' to quit): ")
  
  
print(stringconc)
  
  