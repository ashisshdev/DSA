# in python hashtables ar in built and are called dictionaries

# creating a dictionary
table = {1:"123" , 2:"456" , 3:"789"}

# accessing a value in dictionary by its key
print(table[1])

# inserting a new value in the table
table[4] = "000"
print(table[4])

# updating a existing value
table[2] = "999"
print(table)

# inserting a new value at non-existing key
table[12] = "XoX"
print(table)
# deleting a value from the table
# item at key 3 will be removed 
table.pop(3)

print(table)

# also the entire dictionary can be deleated, using


#other operation such as looping can also be done on dictionaries 

# prints all the keys
print(table.keys())

# prints all the values
print(table.values())


