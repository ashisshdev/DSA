# merge sorted array
# maximum complexity expectd O(a+b)

from array import *

# questions from interviewer
# can there be any negative values?
# can an array be empty?

dummyArray1 = array('i' , (1,2,3,4,5))
dummyArray2 = array('i' , (2,4,6,7,9))
dummyArray3 = array('i' , ())

class Solution():
    def mergeArrays(self,array1,array2) -> array:
        array1Length = len(array1)
        array2Length = len(array2)

        if(array1Length == 0):
            return array2
        if(array2Length == 0):
            return array1
        
        if(array1Length != 0 and array2Length != 0):
            array1Map = {}
            for array1Element in array1:
                if(array1Element not in array1Map):
                    array1Map[array1Element] = 1
                else:
                    array1Map[array1Element] = array1Map[array1Element]+1
            
            for array2Element in array2:
                if(array2Element not in array1Map):
                    array1Map[array2Element] = 1
                else:
                    array1Map[array2Element] = array1Map[array2Element]+1
            
            newArray = array("i" , ())

            for key, value in array1Map.items():
                for x in range(value):
                    newArray.append(key)
            
            print(newArray)

#print(Solution().mergeArrays(array1=dummyArray1,array2=dummyArray2))
# Solution().mergeArrays(array1=dummyArray1,array2=dummyArray2)


class Solution2():
    def mergeSortedArrays(self,array1,array2,array1Length,array2Length):

        mergedArray = array('i' , ())

        if(array1Length == 0):
            return array2
        if(array2Length == 0):
            return array1
        
        i = 1
        j = 1
        array1element = array1[i]
        array2element = array2[j]

        if(array1Length != 0 and array2Length != 0):
            while(array1element or array2element):
                print("while loop started")
                if(array1element == None or array1element > array2element):
                    mergedArray.append(array2element)                        
                    if(j<array2Length-1):
                        try:
                            array2element = array2[j] 
                            j+=1
                        except:
                            array2element = None
                    else:
                        array2element = None
                if (array2element == None or array1element < array2element):
                    mergedArray.append(array2element)                        
                    if(i<array1Length-1):
                        try:
                            array1element = array1[i]
                            i+=1
                        except:
                            array1element = None
                    else:
                        array1element = False

            print(mergedArray)

Solution2().mergeSortedArrays(array1=dummyArray1,array2=dummyArray2 , array1Length= 5,array2Length=5)







