# Basiaclly a fucntion calling itself.
# we used it to traverse linked-lists and trees 

# 1 Common problem with recursion is Stack Overflow 
# A stack overflow is a type of buffer overflow error that occurs when a computer program tries to use more memory space in the call stack than has been allocated to that stack
# i.e. Basically when a function is called so many times that the memory allocated for that process runs out but function does not completes.
# In ./1data structures/user-defined/stack/stack.txt we discussed how OS uses Stack to keep track of the processes
# well in recursion, processess grows so much that stack starts overflowing with them

# some examples are:

# Fibonacci series : 
def fibonacci(upTo:int):
    if(upTo<=1):
        return upTo
    else:
        return fibonacci(upTo-1)+fibonacci(upTo-2)

print(fibonacci(8))
print(fibonacci(5))

print()

# Factorial of n : 
def factorial(n:int) -> int:
    def facto(n:int) -> int:
        if(n>1):
            return n * factorial(n-1)
        elif(-1>n):
            return n * factorial(n+1)
        else: return 1
    
    if(n>0): return facto(n)
    else: return -1*facto(n*-1)


print(factorial(n=5))
print(factorial(n=3))

print(factorial(n=2))
print(factorial(n=1))

print(factorial(n=-4))
print(factorial(n=-3))

print()

# reverse a string 
def reverseString(input:str):
    if(len(input) == 0):
        return input
    else:
        return reverseString(input[1:])+input[0]

print(reverseString("hellow"))


# turns out, we can always use loops to get the same results as we get with recursion 
# but then why the idea of recursion exist at all?
# 1 -> DRY, Recursion allows programmers to follow the Don't Depeat Yourself principle
# 2 -> Readable, its easy to understand rather than multiple nested if's and loops
# 3 -> Useful in cases where we don't know the extent of data/function calls. Like traversing trees and linkedLists. 

# Drawbacks 
# 1 -> Confusing for begineers 
# 2 -> StackOverflow, comes at a cost of increased space complexity 

# When to use recursion Rules
# - Everytime we are utilising a tree or converting something into a tree or graph (or traversing in them)
# - divide and conquer algorithms (Merge sort,Quick sort)




