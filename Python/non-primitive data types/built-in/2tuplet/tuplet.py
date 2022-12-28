# tuplets are just like lists but they are immutable 
# that is, they are created once and can not be changed
# we cannot change, add or remove items after the tuple has been created

# defining a tuplet
my_tuplet = ('hello',1,True,"yolo",69,False,'hello',"orange",'table')
# duplicates are allowed

# CRUD - only creation and reading and nothing else

# common operations on tuplet

# get length of the tuplet
len(my_tuplet) # 9

# count the occurence of a specific element 
my_tuplet.count('Hello') # 0
my_tuplet.count(False) # 1
my_tuplet.count('hello') # 2

# get index of a specific element
my_tuplet.index(69) # 4

# iterating through elements 
for element in my_tuplet:
    element
