password = input("Please enter the password: ")
upper_count = 0
lower_count = 0
number_count = 0
if len(password)<8:
  print("Password is not valid")

else:
  for element in password:
    if element.isdigit():
      number_count += 1

    else:
      if element.isalpha():
        if element.isupper():
          upper_count += 1

        elif element.islower():
          lower_count += 1

  if (upper_count > 0) and (lower_count>0) and (number_count>0):
    print("password is valid")

  else:
    print("password is not valid")

