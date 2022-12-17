# chapter 6, lesson 7
# reverse a string

from array import *

def reverseStringMethod1(strInput:str) -> str:
    strArray = array("u" , list(strInput))
    lengthOfArray = len(strArray)
    reversedArray = array('u',())
    for x in range(lengthOfArray):
        reversedArray.append(strArray[lengthOfArray-1-x])
    return reversedArray

print(reverseStringMethod1("Hello Sir, This is a String."))

print()

# its python so there must be an easier way
someString = "Hello Sir, This is a String."
print(someString[::-1])

print()