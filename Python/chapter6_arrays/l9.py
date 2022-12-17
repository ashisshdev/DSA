from array import *

dummyArray1 = array('i' , (1,2,3,5))
dummyArray2 = array('i' , (3,4))

haha1 = array('i' , (1,2,2,3,4,6,9))
haha2 = array('i' , (2,4,4,6,7,8))

class Solution():
    def mergeSortedArrays(self,array1 :array,array2 :array,lenght1 :int,length2 :int) -> array:
        if(lenght1 == 0):
            return array2
        if(length2 == 0):
            return array1

        mergedArray = array('i' , ())
        i=0
        j=0
        array1Element = array1[i]
        array2Element = array2[j]

        if(lenght1 != 0 and length2 != 0):
            while(array1Element or array2Element):
                print(mergedArray)
                if(array1Element == None or array1Element >= array2Element):
                    mergedArray.append(array2Element)
                    if(j<length2-1):
                        j += 1
                        array2Element = array2[j]
                    else :
                        array2Element = None
                if(array2Element == None or array1Element < array2Element ):
                    mergedArray.append(array1Element)
                    if(i<lenght1-1):
                        i += 1
                        array1Element = array1[i]
                    else:
                        array1Element = None
        else:
            return mergedArray

        return mergedArray;

print(Solution().mergeSortedArrays(array1= dummyArray1,array2=dummyArray2,lenght1=4,length2=2 ));

print(Solution().mergeSortedArrays(array1= haha1,array2=haha2,lenght1=7,length2=6 ));



