# simplest but least efficient 
# Time complexity O(n^2), Space Complexity O(1)

numbers = [5,3,7,9,2,6,67,8,1]

# numbers = [12,5,3,9,7]

def bubbleSort(numbers):
    length = len(numbers)
    for i in range(length):
        # to see the process uncomment below line
        print(numbers)
        for j in range(length-1):
            if numbers[j] > numbers[j+1]:
                # swapping the numbers
                numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
    return numbers 

print(bubbleSort(numbers))


