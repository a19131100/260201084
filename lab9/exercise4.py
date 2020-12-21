import time
def simple_timer(t):
  if t == 0:
    time.sleep(1)
    print("alert!")
  else:
    time.sleep(1)
    print(t)
    return simple_timer(t-1)

simple_timer(5)