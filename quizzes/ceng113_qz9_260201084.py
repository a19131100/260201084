str1 = input("Enter the first letter")
str2 = input("Enter the second letter")
def isAnagram(str1, str2):
  count = 0
  for i in str1:
    for j in str2:
      if i == j:
        count += 1

  if count== len(str1):
    print("They are anagrams")

  else:
    print("They are not anagrams")