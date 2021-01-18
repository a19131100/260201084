my_list = [22, 8, 12, -4, 27, 30, 36, 50, 7, 68, 91, 56, 2, 85, 42, 98, 25]

def selection_sort(a_list):
  
  n = len(a_list)
  for left in range(n):
    min_index = left

    for right in range(left+1, n):
      if a_list[min_index] > a_list[right]:
        min_index = right
    
  a_list[left], a_list[min_index] = a_list[min_index], a_list[left]


  print(a_list)

selection_sort(my_list)