year= int(input("Please enter the year: "))

if year%4==0:
  if year%400!=0:
    print("It's a century year, not a leap year")
  else:
    print("It's a leap year")

else:
  print("It's not a leap year")