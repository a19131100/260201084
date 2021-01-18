def binary_search(arr, low, high, item):
  if high < low:
    return -1

  else:
    mid = (high+low) // 2

    if arr(mid) == item:
      return mid

    elif arr(mid) > item:
      return binary_search(arr, low, mid-1, item)

    else:
      return binary_search(arr, mid+1, high, item)

result = binary_search(my_list, 0, len(my_list),)