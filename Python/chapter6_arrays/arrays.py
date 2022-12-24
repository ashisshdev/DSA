

# to use arrays in python use import array as arr OR from array import *

from array import *

arr1 = array('i' , (1,2,3,4,5))
list1 = [1,2,3,4,5,6]

print(type(arr1))
print(type(list1))

# this is a signer integer array (that can hold all -ve and +ve integers)
signedIntArray = array('i' , (-3,-2,-1,0,1,2,3,4,5))
print(signedIntArray)

# this is a unsigned integer array (that can hold only +ve integers)
unsignedArray = array('I' , (0,1,2,3,4,5))
# this will throw exception -> unsignedArray = array('I' , (-3,-2,-1,0,1,2,3,4,5))
print(unsignedArray)

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
print(floatingNumbers)

print("\n\n\n\n")

print("Operations on Arrays in Python and their BigO :- \n")

print("Creaing an array of character type - time bigO(1) , space bigO(n) ")
arrayForVariousOperation = array('u'  , ('a','b','c','d','m','n','o','p'))

# printing original array
print ("The new created array is : ", end =" ")
for i in range (0, len(arrayForVariousOperation)):
    print (arrayForVariousOperation[i], end =" ")

print("\n")

print("Accessing an element in the array - time BigO(1) , space BigO(1)")
print(f"Elemnent at index 3 is : {arrayForVariousOperation[2]}")
print(f"Elemnent at index 6 is : {arrayForVariousOperation[5]}")

print()

print("inserting into the aray - time bigO(1)/BigO(n) , space BigO(1)")
#two methods are utilised to add elements to the array
print("using method 1 - insert , complexity BigO(n)")

arrayForVariousOperation.insert(4,"x")
print ("New array is : ", end =" ")
for i in range (0, len(arrayForVariousOperation)):
    print (arrayForVariousOperation[i], end =" ")

print()
print("using method 2 - append , complexity BigO(1)")
arrayForVariousOperation.append("y")
print ("New array is : ", end =" ")
for i in range (0, len(arrayForVariousOperation)):
    print (arrayForVariousOperation[i], end =" ")

print("\n")

print("deleting from the array - time bigO(1)/BigO(n) , space BigO(1)")
#two methods are utilised to add elements to the array
print("using method 1 - remove, complexity BigO(n)")
arrayForVariousOperation.remove("o")
print("Array after removing element at position 8 : " , end= " ")
for i in range (0, len(arrayForVariousOperation)):
    print (arrayForVariousOperation[i], end =" ")
print()
print("using method 1 - pop, complexity BigO(1)")
arrayForVariousOperation.pop()
print("Array after using .pop method : " , end= " ")
for i in range (0, len(arrayForVariousOperation)):
    print (arrayForVariousOperation[i], end =" ")

print("\n")
print("searching in an array - time BigO(n) , space BigO(1)")
print("index of first occurance of letter m is : " , end= str(arrayForVariousOperation.index('m')))

print("\n")
print("updating in an array - time BigO(n) , space BigO(1)")
arrayForVariousOperation[3] = "q";
print("array after updaing position 3 with letter q : " ,end= " ")
for i in range (0, len(arrayForVariousOperation)):
    print (arrayForVariousOperation[i], end =" ")
print("\n")

