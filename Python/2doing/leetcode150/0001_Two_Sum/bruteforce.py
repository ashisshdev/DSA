nums = [1,2,3,4,5,1,7,8,9]

def lmaoFunction(numbersList:list):
    for i in range(len(numbersList)-2):
        tempSum1 = numbersList[i]+numbersList[i+1]
        tempSum2 = numbersList[i+1]+numbersList[i+2]

        if(sum==10):
            return i
    return False

print(lmaoFunction(nums))

# adding dynamic programming 
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