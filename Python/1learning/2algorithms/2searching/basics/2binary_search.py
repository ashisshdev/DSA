# Binary search - Divide and conquer

# generating a sorted list with elements from 1-1000 
numbers = []
for i in range(1000):
    numbers.append(i+1)

# global variable so we can count how many times recursive function was called to serach the targeted element 
iterations=0

# returns boolean if target element is found.
def binarySearch(list:list,target:int) -> bool:
    global iterations
    iterations = iterations+1

    midElementIndex = len(list)//2

    if(len(list)>1):
        if(list[midElementIndex] == target):
            print(f"It took {iterations} number of iterations.")
            return True 
    
        elif(target<list[midElementIndex]):
            return binarySearch(list=list[:midElementIndex] , target=target)
        
        elif(target>list[midElementIndex]):
            return binarySearch(list=list[midElementIndex:] , target=target)
    else: 
        print(f"It took {iterations} number of iterations.")
        return False


# # best case, searching element is the middle element of original list - O(1)
iterations=0
print(binarySearch(list=numbers,target=501))

# # average case, searching random element in middle - O(Log(n))
iterations=0
print(binarySearch(list=numbers,target=123))
iterations=0
print(binarySearch(list=numbers,target=789))
iterations=0
print(binarySearch(list=numbers,target=2))

# worst case, searching last element - (O(Log(n)))

# case when the element does not even exist 
iterations=0
print(binarySearch(list=numbers,target=123255))

