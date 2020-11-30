f=open("members.txt", "r")
line = f.readline()
names_dictionary={}

while line != "":
  indx= line.index("@")
  name_tag=email[0:indx]
  names_dictionary[name_tag]= line

print(names_dictionary)
