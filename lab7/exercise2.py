books= ["ULYSSES", "ANIMAL FARM", "BRAVE NEW WORLD", "ENDER'S GAME"]
book_dict= {}

for names in books:
  names1= names.replace(" ", "")
  lengths= (len(names1), len(set(names1)))
  book_dict[names]= lengths

print(book_dict)