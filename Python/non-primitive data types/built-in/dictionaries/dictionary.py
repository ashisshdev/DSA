# dictionaries are what we recognise as maps from other languages
# key-value pairs

# ordered*, changeable and do not allow duplicates.

# creation of a dictionary
dict = {1:'india',2:'japan',2:'china',4:'korea',5:'nepal',6:'bhutan'}

# operations on the Dictionary

# length 
len(dict) #5

## CRUD 
# Insertion
dict[7]='Indonesia'

# Access
dict.get(4)

# get all keys only
dict.keys
# get all values only
dict.values

#iterate over elements
for element in dict:
    element # prints key
    dict[element] # prints value
    dict.get(element) # prints value 
    
for item in dict.keys(): # using keys
    dict.get(item)

for item in dict.values(): # using values
    item

for key,value in dict.items(): # using both
    # key = value
    pass    

# Updating 
dict[3]='hongkong'

# removing items 
# delete specific element
del dict[4] 
dict.pop(2)

# clear dictionary
# dict.clear()
# delete whole damn dictionary
# del dict
