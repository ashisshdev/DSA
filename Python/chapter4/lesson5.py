# // Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items
# //For Example:
# //const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'i'];
# //should return false.
# //-----------
# //const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'x'];
# //should return true.

# // 2 parameters - arrays - no size limit
# // return true or false

## Note that Python does not have built-in support for Arrays, but Python Lists can be used instead. 
## using python lists as arrays here (so dont get confused by variable names)

dummyArray1 = ['a', 'b', 'c', 'x']
dummyArray2 = ['l', 'm', 'x', 'p']

# 1 bruteForce
# loop inside loop, O(n*m) 
def isThereSomethingCommon1(array1,array2):
    for arr1element in array1:
        for arr2element in array2:
            if(arr1element == arr2element):
                return True
    return False

print(isThereSomethingCommon1(array1=dummyArray1,array2=dummyArray2))

def isThereSomethingCommon4(array1,array2):
    array1Map = {}
    for arr1Element in array1:
        if(arr1Element not in array1Map):
            array1Map[arr1Element] = True
    
    for arr2Element in array2:
        if(arr2Element in array1Map):
            return True
    
    return False

print(isThereSomethingCommon4(array1=[],array2=dummyArray2))

def againFunction():
    print("My job is to return and double anything I eceive as an Input hehe")
    

#---------------------------------------

# 2 using Maps 
# two for loops, O(n+m) 
def isThereSomethingCommon2(array1,array2):
    elementsOfArr1Map = {};
    for arr1element in array1:
        if arr1element not in elementsOfArr1Map:
            elementsOfArr1Map[arr1element] = True

    for arr1e2element in array2:
        if arr1e2element in elementsOfArr1Map:
            return True
    return False        

print(isThereSomethingCommon2(array1=dummyArray1,array2=dummyArray2))

#---------------------------------------

# 3 python magic
# complexity same as method 1 , i.e. O(n*m) , but really less code
def isThereSomethingCommon3(array1,array2):
    return any(item in array1 for item in array2)

print(isThereSomethingCommon3(array1=dummyArray1,array2=dummyArray2))

