def get_reserved(a_list):
  if len(a_list) == 0:
    return []
  else:
    return [a_list[-1]] + get_reserved(a_list[:-1])

print(get_reserved([1,2,3]))
