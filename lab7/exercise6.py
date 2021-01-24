numbers1 = [2,3,4,20,5,5,15]
numbers2 = [10,20,20,15,30,40]

numbers1 = set(numbers1)
numbers2 = set(numbers2)

intersection =[]

for member in numbers1:
  if member in numbers2:
    intersection.append(member)

for member in numbers1:
  numbers2.add(member)


print(intersection)
print(numbers2)
