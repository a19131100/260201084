def sum_function(a_list):
  sum_of_elements = 0
  for i in a_list:
    sum_of_elements += i

  return sum_of_elements**2

a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
print(sum_function(a_list))
