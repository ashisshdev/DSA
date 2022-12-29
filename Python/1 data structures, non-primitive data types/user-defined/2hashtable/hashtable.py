# in python hashtables ar in built and are called dictionaries

# creating a table
my_table = {1:"123" , 2:"456" , 3:"789"}

# accessing a value in table by its key
my_table[1] # 123

# inserting a new value in the my_table
my_table[4] = "000"

# updating a existing value
my_table[2] = "999"

# other operation such as looping can also be done on tables 
# but keep in mind that they are un-ordered 
# iterate over elements
for element in my_table:
    element # prints key
    my_table[element] # prints value
    my_table.get(element) # prints value 
    
for item in my_table.keys(): # using keys
    my_table.get(item)

for item in my_table.values(): # using values
    item

for key,value in my_table.items(): # using both
    # print at key = value
    pass 

# deleting a value from the my_table
# item at key 3 will be removed 
my_table.pop(3)
# or 
del my_table[2]

# also the entire table can be deleated, using
del my_table

