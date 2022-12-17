# well queues can be immplemented in several ways 
# 1 using Lists
# 2 using deque library
# 3 using queue library <- we are going to usilise this method

from queue import LifoQueue
# Stack is basically a queue but with LIFO order - (Last In First Out)

# making a static stack with max size
myStaticStack = LifoQueue(maxsize=4)

def fullAndEmptyStatus():
    print("is Empty : " ,end=str(myStaticStack.empty()))
    print()
    print("is Full : " ,end=str(myStaticStack.full()))
    print()
    print()

fullAndEmptyStatus()

myStaticStack.put(1)
myStaticStack.put(2)

fullAndEmptyStatus()

myStaticStack.put(3)
myStaticStack.put(4)

fullAndEmptyStatus()

# just like queues, there's no way to access elements without removing them
# so it goes

for element in range(myStaticStack.qsize()):
    print(myStaticStack.get() , end="   ")
print()
print()

fullAndEmptyStatus()

# similarly we can make dynamic stacks here 
# the only diffrence will be that the .full() will always return False

myDynamicStack = LifoQueue()

myDynamicStack.put(1)
myDynamicStack.put(2)
myDynamicStack.put(3)
myDynamicStack.put(4)
myDynamicStack.put(5)

print("dynamic array size = " , end=str(myDynamicStack.qsize()))
print()
print()
print(f"removing {myDynamicStack.get()}" , end= f"  &  {myDynamicStack.get()}")
print()
print("dynamic array size = " , end=str(myDynamicStack.qsize()))
print()
print()





















































# #static Stack 
# myStaticStack = LifoQueue(maxsize=4) # maximum size parameter is passed

# def fullAndEmptyStatus():
#     print()
#     print("is Empty = " , end=str(myStaticStack.empty()))
#     print()
#     print("is Full = ",end=str(myStaticStack.full()))
#     print() 
#     print()

# fullAndEmptyStatus()

# myStaticStack.put(1)
# myStaticStack.put(2)

# fullAndEmptyStatus()

# myStaticStack.put(3)
# myStaticStack.put(4)

# fullAndEmptyStatus()

# # printing all the elements 
# # just like queues, there is no way to access and iterate through the stack
# # so we have to one by one remove all the elements to see them all 
# for element in range(myStaticStack.qsize()):
#     print(myStaticStack.get() , end="   ")
# print()
# # see the difference in the output, while printing all the elements of a queue
# # we go 1 , 2 , 3 , 4 ; in case of stack we get 4 , 3 , 2 , 1
# # thats FIFO and LIFO 

# fullAndEmptyStatus()

# # a dynamic stack
# # the only difference here will be that full() will always return false 
# # and we can just add as many elements 
# # in case of static Stack if we try to add more elements than the size
# # then it returns error (not an error exactly, it just waits for the momory to free to insert new element)
# myDynamicStack = LifoQueue()




