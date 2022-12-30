# on the concept of divide and conquer
# all complexities are O(n log(n)) but space tradeoff is O(n)

numbers = [4,8,2,7,9,6,0,1]

def mergeSort(array):

    length = len(array)

    if length ==1 :
        return array

    right = array[0:int(length/2)]
    left = array[int(length/2):length]

    return merge(
        mergeSort(left),
        mergeSort(right)
    )


def merge(left,right):
    return 

print(mergeSort(numbers))
