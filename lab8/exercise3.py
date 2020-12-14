import random
def get_rand_list(b, e, N):
  return random.sample(range(b,e), N)

def get_overlap(list1, list2):
  overlapped_list= []
  for i in list1:
    if i in list2:
      overlapped_list.append(i)
  return(overlapped_list)


def main():
  list1 = get_rand_list(0, 10, 5)
  list2 = get_rand_list(0, 10, 5)
  print(list1)
  print(list2)
  print(get_overlap(list1, list2))

main()
