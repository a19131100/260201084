def is_prime(number1):
  if number1>1:
    for i in range(2,number1):
      if number1%2 == 0:
        continue
      else:
        return i

def print_primes_between(int1, int2):
  for x in range(int1, int2):
      if is_prime(x):
        print(x, end=" ")

def main():
  integer1= int(input("Please enter the first number:"))
  integer2 = int(input("Please enter the second integer:"))
  print_primes_between(integer1,integer2)


main()