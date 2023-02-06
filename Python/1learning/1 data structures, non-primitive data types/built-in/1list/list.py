# declaration of a list
furniture = ['table', 'chair', 'rack', 'shelf','lamp','stool','sofa','beanbag']

## functions on lists in python
#CRUD - Create/Insert , Read/Access , Update/Patch , Delete/Remove 

# Inserting elements
furniture.append('extention') # adds in the end 
furniture.insert(3,'stand') # inserts 'stand' at element 3 and shift all the elemnts by 1 

# accessing elements in the list
furniture[0] # 'table'
furniture[1] # 'chair'
furniture[-2] # 'sofa'

# creating sublists 
new_sublist = furniture[2:6] #['rack', 'shelf', 'lamp', 'stool']
# 2 is inclusive and 6 is exclusive

# changing elements
furniture[2] = 'bed'
# before - ['table', 'chair', 'rack', 'shelf', 'lamp', 'stool', 'sofa', 'beanbag']
# after - ['table', 'chair', 'bed', 'shelf', 'lamp', 'stool', 'sofa', 'beanbag']

# removing elements
# last element
furniture.pop()
# element at a specific index
del furniture[2]
# a specific element whose index is not known
furniture.remove('chair')
# clears the entire list
# furniture.clear() 

# other operations 

# length of the list
len(furniture) # 7

# looping/iterarting lists
for item in furniture:
    item

# enumerate 
for index, item in enumerate(furniture):
    f'index: {index} - item: {item}'

# in and not in operations
'rack' in ['table', 'chair', 'rack', 'shelf']
# True

'bed' not in ['table', 'chair', 'rack', 'shelf']
# False




