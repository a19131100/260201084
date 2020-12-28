def threemulti(n):
  if n==0:
    return 0
  else:
    return 3 + threemulti(n-1)

print(threemulti(6))