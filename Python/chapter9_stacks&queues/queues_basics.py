# well queues can be immplemented in several ways 
# 1 using Lists
# 2 using deque library
# 3 using queue library <- we are going to usilise this method

from queue import Queue 
# Queues follow FIFO order - (First In First Out)

# Available Operations:
# put() -> Enqueue (insert/append/put in end) ;
# get() -> Dequeue(delete/pop/remove from first) ;
# qsize() ; empty() ; full()


myStaticQueue = Queue(maxsize=5)

def fullAndEmptyStatus():
    print()
    print("is Empty = " , end=str(myStaticQueue.empty()))
    print()
    print("is Full = ",end=str(myStaticQueue.full()))
    print() 
    print()


# lets check queue's full and empty status 
fullAndEmptyStatus()

# insert element
myStaticQueue.put(1)
myStaticQueue.put(2)
myStaticQueue.put(3)

# lets check queue's full and empty status 
fullAndEmptyStatus()

# insert more elements 
myStaticQueue.put(4)
myStaticQueue.put(5)

fullAndEmptyStatus()

# getElements
print(myStaticQueue.get())
print(myStaticQueue.get())

fullAndEmptyStatus()

# printing all the elements 
# well there is no way to access and iterate through the queue so we have to one by one remove all the elements to see them all 
for element in range(myStaticQueue.qsize()):
    print(myStaticQueue.get() , end="   ")
print()

fullAndEmptyStatus()

# the only difference here will be that full() will always return false 
# and we can just add as many elements 
# in case of static Queue if we try to add more elements than the size
# then it returns error 
myDynamicQueue = Queue()

