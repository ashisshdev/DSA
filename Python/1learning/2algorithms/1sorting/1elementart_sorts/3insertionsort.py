# Same as previous two

# Time complexity O(n^2), Space Complexity O(1)

numbers = [5,3,7,9,2,6,67,8,1]

# numbers.insert(4,99)
# numbers.remove(99)

def insertSort(numbers):
    length = len(numbers)
    for i in range(length):
        # decrementing loop from i to 0
        for j in range(i,0,-1):
            if numbers[j]<numbers[j-1]:
                numbers[j-1],numbers[j]=numbers[j],numbers[j-1]
    return numbers

print(insertSort(numbers))

# one advantage is that it performs really really well with small data sets 
# or when the list is nearly sorted 
