def hailstone(n):
  if n == 1:
    return str(n)
  if n % 2 == 0:
    return str(n) + "," + hailstone(n/2)
  else:
    print(int(3*n +1))
    return str(n) + "," + hailstone(3*n + 1)

print(hailstone(5))
  