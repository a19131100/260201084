number_list= []
num_of_elements= int(input("How many number?: "))

for i in range(num_of_elements):
  items= int(input("Enter the number: "))
  number_list.append(items)

unique_list= list(set(number_list))
unique_list.sort()
reversed_list= unique_list[::-1]

print(reversed_list)

