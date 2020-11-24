length= int(input("Please enter a number for identity matrix: "))
matrix=[]

for row in range(length):
  matrix.append( [0]* length)
  matrix[row][row]= 1

print(matrix)  

