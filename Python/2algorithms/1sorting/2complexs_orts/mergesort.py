# on the concept of divide and conquer
# all complexities are O(n log(n)) but space tradeoff is O(n)

# helper function 
def insertSort(numbers):
    length = len(numbers)
    for i in range(length):
        # decrementing loop from i to 0
        for j in range(i,0,-1):
            if numbers[j]<numbers[j-1]:
                numbers[j-1],numbers[j]=numbers[j],numbers[j-1]
    return numbers


# test 
numbers = [0,4,2,6,7]
numbers2 = [4,2,15,7,3,69]
numbers3 = [4,8,2,7,9,6,0,1,11,45,1,]

def mergeSort(array):

    length = len(array)

    if length ==1 :
        return array

    left = array[0:int(length/2)]
    right = array[int(length/2):length]

    return merge(
        mergeSort(left),
        mergeSort(right)
    )

def merge(left,right):
    if(left is None):
        return right
    if(right is None):
        return left

    # ------------------------------------------------------------------
    # leftLength = len(left)
    # rightLength = len(right)    
    # # creating an array of left+right elements size 
    # sortedArray = [None] * (leftLength+rightLength)
    # print(sortedArray)
    # leftindex = 0
    # rightindex = 0

    # while(leftindex < leftLength and rightindex < rightLength):
    #     if left[leftindex] < right[rightindex]:
    #         sortedArray.append(left[leftindex])
    #         leftindex = leftindex+1
    #     else:
    #         sortedArray.append(right[rightindex])
    #         rightindex = rightindex+1

    # return sortedArray
    # ------------------------------------------------------------------
    # we will utilise insertion sort here becuase of the advantages we discussed earlier
    # 1 its great on small datasets 
    # 2 its great with nearly sorted datasets 
    combinedArray = left+right
    return insertSort(combinedArray);

print(mergeSort(numbers))
print()
print(mergeSort(numbers2))
print()
print(mergeSort(numbers3))
