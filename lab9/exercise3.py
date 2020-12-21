def get_evens(a_list):
  if len(a_list) == 0:
    return 0
  else: 
    counter = 0
    if a_list[0] % 2 == 0:
      counter = 1
      
  return counter + get_evens(a_list[1:])

print(get_evens([1,2,3,4,5,6]))