def isAnagram(str1, str2):
  if len(str1) == 0:
    return 0

  else:
    counter = 0
    if str1[-1] == str2[0]:
      counter 1

  return counter + isAnagram(str1[:-1], str2[1:])