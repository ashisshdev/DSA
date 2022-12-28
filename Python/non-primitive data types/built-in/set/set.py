# creating a set
my_set = {'india',420,'japan',False,'china',123,'korea','nepal',False,'bhutan',True,123,'korea'}

# length
len(my_set) #10 - duplicate items will be ignored

# adding/inserting new elements
my_set.add('hongkong')
# adding multiple items
my_set.update([False,"china",'italy','india'])
# adding one set in another
my_set.update({'iran',False,'iraq',420})

# everytime we try to access a set, the items order will be changed
print(my_set)

# iterating 
for item in my_set:
    item
# checking if a element exist 
'australia' in my_set

# we can not do my_set(some_element) = new_value
# or my_set[some_key] = new_value

# Removing 
my_set.remove('india') # remove specific element 
my_set.pop() # remove a random element 

# clear set
my_set.clear()


