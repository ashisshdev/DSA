from array import *

dummyArray1 = array('i' , (1,2,3,4,5,))
dummyArray2 = array('i' , (2,4,6,7,9))

class Solution2():
    def mergeSortedArrays(self,array1,array2,array1Length,array2Length):

        mergedArray = array('i' , ())

        if(array1Length == 0):
            return array2
        if(array2Length == 0):
            return array1
        
        i = 0
        j = 0
        array1element = array1[i]
        array2element = array2[j]

        print("hehe 1")

        if(array1Length != 0 and array2Length != 0):
            print("hehe 2")
            while(array1element or array2element):
                print(array1element)
                print(array2element)
                print("hehe 3")
                if(array1element < array2element):
                    mergedArray.append(array1element)
                    array1element = array1[i+1]
                else:
                    mergedArray.append(array2element)
                    array2element = array2[j+1]
            print(mergedArray)
            print("hehe 4")
        print(mergedArray)
        print("hehe 5")

#Solution2().mergeSortedArrays(array1=dummyArray1,array2=dummyArray2 , array1Length= 5,array2Length=5)


def hehe(array1,array2,array1Length,array2Length):

    i = 0
    j = 0
    array1element = array1[i]
    array2element = array2[j]

    mergedArray = array('i' , ())
    if(array1Length != 0 and array2Length != 0):
            print("hehe 2")
            while(array1element and array2element):
                if(array1element < array2element):
                    mergedArray.append(array1element)
                    try:
                        array1element = array1[i]
                        i+=1
                    except:
                        array1element = False
                        pass
                else:
                    mergedArray.append(array2element)
                    array2element = array2[j]
                    j+=1

            print(mergedArray)
            print("hehe 4")


hehe(array1=dummyArray1,array2=dummyArray2,array1Length=5,array2Length=5)