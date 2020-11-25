length= int(input("Write a number for the matrix: "))
matrix=[]
for i in range(length):
  matrix.append([0] * length)

for row in range(length):
  for coloumn in range(length):
    num= int(input("Please enter a number: "))
    matrix[row][coloumn]= num

sum_of_main=0
for i in range(length):
  sum_of_main += matrix[i][i]

for i in matrix:
  print(i)

print("The sum of the main diagonal is: ", sum_of_main)