books= ["ULYSSES", "ANIMAL FARM", "BRAVE NEW WORLD", "ENDER'S GAME"]
book_dict= {}

for names in books:
  lengths= (len(names), len(set(names)))
  book_dict[names]= lengths

print(book_dict)