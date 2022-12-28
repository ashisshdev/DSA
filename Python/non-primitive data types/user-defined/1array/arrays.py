# to use arrays in python use import array as arr OR from array import *

from array import *

arr1 = array('i' , (1,2,3,4,5))
list1 = [1,2,3,4,5,6]

type(arr1) # <class 'array.array'>
(type(list1)) # <class 'list'>

# Different type of Arrays 
# this is a signer integer array (that can hold all -ve and +ve integers)
signedIntArray = array('i' , (-3,-2,-1,0,1,2,3,4,5))
# print(signedIntArray) 
# >> array('i', [-3, -2, -1, 0, 1, 2, 3, 4, 5])

# this is a unsigned integer array (that can hold only +ve integers)
unsignedArray = array('I' , (0,1,2,3,4,5))
# this will throw exception -> unsignedArray = array('I' , (-3,-2,-1,0,1,2,3,4,5))
# print(unsignedArray)
# >> array('I', [0, 1, 2, 3, 4, 5])

'''
Different types of symbols for arrays that can be build in python and theri python data types 
'b'	signed char 	int
'B'	unsigned char	int
'u'	wchar_t	Unicode character
'h'	signed short	int	
'H'	unsigned short	int	
'i'	signed int	    int	
'I'	unsigned int	int	
'l'	signed long	    int	
'L'	unsigned long	int	
'q'	signed long long	int	
'Q'	unsigned long long	int	
'f'	float	        float
'd'	double	        float
'''

floatingNumbers = array('d',[10.0,20.0,30.0])
# print(floatingNumbers)
# >> array('d', [10.0, 20.0, 30.0])

#-------------------X-------------------

## Operations on Arrays and their BigO

# Creaing an array of character type - time bigO(1) , space bigO(n)
arrayForVariousOperation = array('u'  , ('a','b','c','d','m','n','o','p'))

# Inserting new elements 
# using method 1 - insert ,time BigO(n) , space BigO(1)
# inserts x at position 4 and shifts every element by +1
arrayForVariousOperation.insert(4,"x")
# using method 2 - append ,time BigO(n) , space BigO(1)
# inserts y at the end 
arrayForVariousOperation.append("y")

# Accessing an element in the array - time BigO(1) , space BigO(1)
arrayForVariousOperation[2] # >> c
arrayForVariousOperation[5] # >> n

# iterating through the elements 
for element in arrayForVariousOperation:
    element

# Updating elements 
# updating in an array - time BigO(n) , space BigO(1)
arrayForVariousOperation[3] = "q";

# deleating elements from array
# using method 1 - remove, time BigO(n) , space BigO(1)
# deleates element and shifs all others by -1
arrayForVariousOperation.remove("o")
# using method 2 - pop, time BigO(1) , space BigO(1)
# deleates last element in the array
arrayForVariousOperation.pop()
