
# # uncomment this to run code, dont uncomment all at once
# # -----------------------------------------------------------------------------------
# # 👆 long dash lines like this divides different examples

# import time

# def addToNumbers(a,b) :
    
#     print(f"function is calculating the value of {a} + {b} ...")
#     # assume there is a complex process going on ..
#     time.sleep(2)
#     c = a+b
#     # after 2 some time and calculating the result .. 
#     print(f"value calculated successfully, result = " , end= "")
#     return c

# # everytime we have to add two values we will utilise this function
# print(addToNumbers(2,3))
# # now we know that the a similar problem was solved but the function will again re-calculate everything and take its time
# print(addToNumbers(4,1))

# print()
# print("We can improve this by using the concept of dynamic programming, that is storing the solutions of similar problems ")
# print()

# # 

# cachedSolutions = {}
# def addToNumbersImproved(a,b) :
#     print(f"function is calculating the value of {a} + {b} ...")
#     if(a+b in cachedSolutions):
#         print(f"value calculated successfully, result = " , end= "")
#         return cachedSolutions[a+b]    
#     else :
#         # assume there is a complex process going on ..
#         time.sleep(2)
#         c = a+b
#         # after 2 some time and calculating the result .. 
#         print(f"value calculated successfully, result = " , end= "")
#         cachedSolutions[a+b]=c
#         return cachedSolutions[a+b] 

# # this time, the value of 2+3 operation takes time
# print(addToNumbersImproved(2,3))
# # but the value of 4+1 is caculated instantly because its already cached 
# print(addToNumbersImproved(4,1))
# # this is how we prevent time and resources by storing similar problem's solutions 

# print()
# print()

# # 

# # we can further improve this code by not making the cachedSolutions global and preventing polluting the global scope 
# def addToNumbersImproved() :
#     # storing solutions in function's scope and not global scope 
#     cachedSolutions = {}
#     def function (a,b):
#         print(f"function is calculating the value of {a} + {b} ...")
#         if(a+b in cachedSolutions):
#             print(f"value calculated successfully, result = " , end= "")
#             return cachedSolutions[a+b]    
#         else :
#             # assume there is a complex process going on ..
#             time.sleep(2)
#             c = a+b
#             # after 2 some time and calculating the result .. 
#             print(f"value calculated successfully, result = " , end= "")
#             cachedSolutions[a+b]=c
#             return cachedSolutions[a+b] 
#     return function

# addTwoNumbersFunctionality = addToNumbersImproved()
# print(addTwoNumbersFunctionality(2,3))
# print(addTwoNumbersFunctionality(4,1))

# print()



# --------------------------------------------------------------------------------------------------------

## Example 2 - finding nth number in fibonacci series  
# 0, 1, 2, 3, 4, 5, 6,  7,  8, 9,  10, 11, 12,   13,  14 , ...
# # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377 , ...

## UnOptimised example to show how bad recursion can be 

calculationsCycles = 0 # basically how many times a function recursed 

def fibonacci(n): # recursive function 
    global calculationsCycles
    calculationsCycles = calculationsCycles+1
    if(n<2):
        return n
    else: return fibonacci(n-1)+fibonacci(n-2)

print(f"fibonacci of 7 = {fibonacci(7)}")
print(f"Total recursions took for fibonacci of 7 = {calculationsCycles}")
print(f"fibonacci of 20 = {fibonacci(20)}")
print(f"Total recursions took for fibonacci of 20 = {calculationsCycles}")

# Lets improve above code using dynamic programming 

recursionCyclesOptimised = 0

def fibonacciOptimised():
    cachedSolutions = {}
    def fib(n):
        global recursionCyclesOptimised
        recursionCyclesOptimised = recursionCyclesOptimised+1
        if(n in cachedSolutions):
            return cachedSolutions[n]
        else:
            if(n<2):
                return n
            else: 
                cachedSolutions[n] = fib(n-1)+fib(n-2)
                return cachedSolutions[n]
    return fib

fibonacciFunctionality = fibonacciOptimised()
print(f"fibonacci of 7 = {fibonacciFunctionality(7)}")
print(f"Total recursions took for fibonacci of 7 = {recursionCyclesOptimised}")
print(f"fibonacci of 20 = {fibonacciFunctionality(20)}")
print(f"Total recursions took for fibonacci of 20 = {recursionCyclesOptimised}")

## Try running the code below and see the delay
## moreover, increase the number 35 to 50 or 100 and the slow function will crash the system

# print(f"fibonacci of 35 using slow function = {fibonacci(35)}")
# print(f"Total recursions took for fibonacci of 35 = {calculationsCycles}")
# print("\n")
# print(f"fibonacci of 35 using dynamc programming = {fibonacciFunctionality(35)}")
# print(f"Total recursions took for fibonacci of 35 = {recursionCyclesOptimised}")
