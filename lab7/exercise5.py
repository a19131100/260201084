user_password = "abc123"
counter = 0
while True:
  checking_password = input("Please enter the password:")
  if checking_password == user_password and counter<=2:
    print("You have successfully logged in")
    break
  elif checking_password != user_password and counter<2:
    print("Sorry, the password is wrong")
    counter += 1
    continue
  elif checking_password != user_password and counter == 2:
    print("Sorry, the password is wrong")
    print("You have been denied access")
    break