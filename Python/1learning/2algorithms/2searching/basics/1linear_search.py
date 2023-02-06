# Linear search  - visit each element one by one until taget is found

# generating a sorted list with elements from 1-1000 
numbers = []
for i in range(1000):
    numbers.append(i+1)

# returns boolean if target element is found.
def linearSearch(list:list,target:int):
    for i in range(len(list)):
        if list[i] == target:
            print(f"Found element after {i} iterations.")
            return True
    print("Target element does not exist.")
    return False

# best case, searching first element 
print(linearSearch(list=numbers,target=33))

# average case, searching random element in middle 
print(linearSearch(list=numbers,target=435))
print(linearSearch(list=numbers,target=297))
print(linearSearch(list=numbers,target=1872))
print(linearSearch(list=numbers,target=689))

# worst case, searching last element 
print(linearSearch(list=numbers,target=998))

