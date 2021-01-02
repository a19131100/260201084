def security(password):
  level = 0
  if (len(password)<8) or (" " in password):
    return level
  else:
    for i in password:
      if i.isdigit():
        level += 1
        break
    for y in password:
      if y.isalpha():
        level += 1
        break

    for z in password:
      if z.isdigit():
        continue
      elif z.isalpha():
        continue
      else:
        level += 1
        break
  return level   
def main():
  password = input("Enter your password: ")
  print("Level", security(password))

main()
  
