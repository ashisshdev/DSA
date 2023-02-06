# implemented with help from
# https://www.youtube.com/watch?v=7h1s2SojIRw&ab_channel=AbdulBari
# and https://www.javatpoint.com/quick-sort

# test cases
numbers = [3,4,2,7,5]
numbers2 = [11,4,2,15,7,3,69,72,55]
numbers3 = [4,8,2,7,9,6,0,1,11,45,1,]

def partition(array,start,end):
    # lets assume that pivot is the first element
    pivot = array[start]
    i = start+1
    j = end

    # while j is bigger than i 
    # that is the both ends are yet to meet 
    while i<j:

        # increase i if element at i is smaller then or equal to pivot 
        # do{i++} while: array[i] <= pivot
        while True:
            if array[i] >= pivot:
                break
            else:
                i=i+1
        
        # decrease j if element at j is larger then or equal to pivot 
        # do{j--} while: array[j] >= pivot
        while True:
            if array[j] <= pivot:
                break
            else:
                j=j-1
        # code will reach this line only if [i] is bigger than pivot and [j] is smaller than pivot 
        # therefor, for current values of i and j 
        # if i is smaller than j i.e. they are apart from meeting each other 
        # then swap them
        if(i<j):
            array[i],array[j] = array[j],array[i] 

    # finally we replace the first element (our assumed pivot) with the element at actual pivot position we just derived 
    array[start],array[j] = array[j],array[start]
    # and we return the position of the pivot so we can break array and again perform quicksort
    return j


def quickSort(array,lowest,highest):
    # if array have atleast 2 elements 
    if(lowest<highest):
        pivot = partition(array,lowest,highest)
        quickSort(array,lowest,pivot-1)
        quickSort(array,pivot+1,highest)
    else:
        return array

print("arrays before sorting : ")
print(numbers)
print(numbers2)
print(numbers3)

quickSort(numbers,0,len(numbers)-1)
quickSort(numbers2,0,len(numbers2)-1)
quickSort(numbers3,0,len(numbers3)-1)

print('------------')
print("arrays after sorting :" )
print(numbers)
print(numbers2)
print(numbers3)


# ==========================================================
# # one issue is that python do not have do-while loops
# # therefore I have simple solution of my own 
# # uncomment the code below to make it work
# i=0
# array = [10,6,8,11,4,15,3,18,19]
# pivot = array[0]

# while True:
#     if(array[i]>pivot):
#         break
#     else:
#         i=i+1

