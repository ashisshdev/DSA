# same as bubble sort
# Time complexity O(n^2), Space Complexity O(1)

numbers = [5,3,7,9,2,6,67,8,1]

def selectionSort(numbers):
    length = len(numbers)
    for i in range(length):
        # uncomment below line to see process
        # print(numbers)

        # lets assume that current element is the smallest
        smallest = i
        # only looping in elemnts that are left unsorted 
        # i.e from i to length
        for j in range(i,length):
            if(numbers[j]<numbers[smallest]):
                # updating the smallest element 
                smallest = j

        # swapping the numbers
        numbers[i],numbers[smallest] = numbers[smallest],numbers[i]

    return numbers

print(selectionSort(numbers))
