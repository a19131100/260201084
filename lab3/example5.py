month= input("Which month is it?")
day= int(input("Which day is it?"))


if (month == "march" and day>= 20) or month== "april" or month=="may" or (month== "june" and day<21):
  print("It's Spring")

elif (month == "june" and day>=21) or month=="july" or month=="august" or (month== "september" and day<22):
  print("It's Summer")

elif (month=="september" and day>=22) or month=="october" or month=="november" or (month=="december" and day<21):
  print("It's Fall")

else:
  print("It's Winter")