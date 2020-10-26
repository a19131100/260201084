age= int(input("How old are you?:"))
price= 3

if age<6 or age>60:
  print("Ticket is free!")

elif 6<age<18:
  price= price * (50/100)
  print("The price of the ticket is:", price)

else:
  print("The price of the ticket is:", price)
