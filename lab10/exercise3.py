def sum_of_list(a_list):
  if len(a_list) == 0:
    return 0
  else:
    if isinstance(a_list[0], list):
      summ = 0
      for i in a_list[0]:
        summ += i
      return summ + sum_of_list(a_list[1:])
    else:
      return a_list[0] + sum_of_list(a_list[1:])

print(sum_of_list([3,12,76,[4,56,43],[2,8],81,75]))