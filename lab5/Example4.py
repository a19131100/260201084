password= "abc123"
x=0

while True:
  checker= input("Please enter the password, if you want help write help")
  
  if checker== "help":
    print(password[x])
    x+=1
  
  elif checker!= password:
    print("Wrong password")
  
  else:
    print("Welcome")
    exit()


