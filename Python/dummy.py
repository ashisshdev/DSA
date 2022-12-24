# from array import *

# dummyArray1 = array('i' , (1,1,2,3,3,4,5))
# dummyArray2 = array('i' , (2,4,6,7,9))

# class Solution2():
#     def mergeSortedArrays(self,array1,array2,array1Length,array2Length):

#         mergedArray = array('i' , ())

#         if(array1Length == 0):
#             return array2
#         if(array2Length == 0):
#             return array1
        
#         i = 0
#         j = 0
#         array1element = array1[i]
#         array2element = array2[j]

#         print("hehe 1")

#         if(array1Length != 0 and array2Length != 0):
#             print("hehe 2")
#             while(array1element or array2element):
#                 print(array1element)
#                 print(array2element)
#                 print("hehe 3")
#                 if(array1element < array2element):
#                     mergedArray.append(array1element)
#                     array1element = array1[i+1]
#                 else:
#                     mergedArray.append(array2element)
#                     array2element = array2[j+1]
#             print(mergedArray)
#             print("hehe 4")
#         print(mergedArray)
#         print("hehe 5")

# #Solution2().mergeSortedArrays(array1=dummyArray1,array2=dummyArray2 , array1Length= 5,array2Length=5)


# def hehe(array1,array2,array1Length,array2Length):

#     i = 0
#     j = 0
    
#     array1element = array1[i]
#     array2element = array2[j]

#     mergedArray = array('i' , ())
#     if(array1Length != 0 and array2Length != 0):
#         # here I have to check if there is an element at arra1element 
#             print("hehe 2")
#             while(array1element or array2element):
#                 print("hehe 3")
#                 if(array1element < array2element or array2element):
#                     mergedArray.append(array1element)
#                     if(i<array1Length):
#                         try:
#                             array1element = array1[i]
#                             i+=1
#                         except:
#                             array1element = None
#                     else:
#                         array1element = False

#                 elif(array1element > array2element or array1element):
#                     mergedArray.append(array2element)
#                     if(j<array2Length):
#                         try:
#                             array2element = array2[j]
#                             j+=1
#                         except:
#                             array1element = None
#                     else:
#                         array2element = False
#             print(mergedArray)

# # hehe(array1=dummyArray1,array2=dummyArray2,array1Length=5,array2Length=5)

# dummyArray1 = array('i' , (1,1,2,3))

# def someFunction(array1:array):
#     arrayElement = array1[0]
#     i=1
#     while (arrayElement):
#         # append function here 
#         if(i<=len(array1)):
#             # print(i-1)
#             try:
#                 arrayElement = array1[i]
#                 i=i+1
#             except:
#                 arrayElement = None
#         else:
#             arrayElement = None

# someFunction(array1=dummyArray1)

class Node():
    def __init__(self , value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self , initialNodeValue):
        if(initialNodeValue is None):
            self.root = None
        else :
            self.root = Node(value=initialNodeValue)
    
    def insert(self,value):
        currentNode = self.root
        while value :
            if(value == currentNode.value):
                raise "Duplicate Value Detected !"
            elif (value < currentNode.value):
                if(currentNode.left):
                    currentNode = currentNode.left
                else :
                    currentNode.left = Node(value)
                    value = None
            else:
                if(currentNode.right):
                    currentNode = currentNode.right
                else :
                    currentNode.right = Node(value)
                    value = None

    def lookUp(self,value):
        currentNode = self.root
        while value:
            if(currentNode.value == value):
                return True
            elif(currentNode.value > value):
                if(currentNode.left):
                    currentNode = currentNode.left
                else:
                    return False
            else:
                if(currentNode.right):
                    currentNode = currentNode.right
                else:
                    return False
        return False

    def traverseToSpecificIndex():
        pass

    # def replaceAndDelete(self,node):
    #     # case 1 it is leaf
    #     if(node.left == None and node.right == None):
    #         print("removing ",end=str(node.value))
    #         node.value = None 
    #         print(node.value)
    #     # case 2 - left node is null and right node is there 
    #     elif (node.right is not None and node.left is None):
    #         print("replacing with right and removing ",end=str(node.value))
    #         node.value = node.right
    #         node.right = None
    #     elif (node.right is None and node.left is not None):
    #         print("replacing with left and removing ",end=str(node.value))
    #         node.value = node.left
    #         node.left = None
    #     else:
    #         print("both left and right exist lmao")
    #         print(node.right.value)
    #         print(node.left.value)


    # left, root, right
    def traverseInOrder(self,node:Node):
        if(node.left):
            self.traverseInOrder(node.left)
        print(node.value , end='  ')
        if(node.right):
            self.traverseInOrder(node.right)        

    # root, left, right
    def traversePreOrder(self,node:Node):
        print(node.value , end='  ')
        if(node.left):
            self.traversePreOrder(node.left)
        if(node.right):
            self.traversePreOrder(node.right)        

    # left, right, root
    def traversePostOrder(self,node:Node):
        if(node.left):
            self.traversePostOrder(node.left)
        if(node.right):
            self.traversePostOrder(node.right)
        print(node.value,end='  ')
  

# root
myBinaryTree = BinaryTree(25)

# level 1 
# left
myBinaryTree.insert(15)
# right
myBinaryTree.insert(50)

# level 2 
# left
myBinaryTree.insert(10)
myBinaryTree.insert(22)
# right
myBinaryTree.insert(35)
myBinaryTree.insert(70)

# level 3
# left
myBinaryTree.insert(4)
myBinaryTree.insert(12)
myBinaryTree.insert(18)
myBinaryTree.insert(24)
# right
myBinaryTree.insert(31)
myBinaryTree.insert(44)
myBinaryTree.insert(66)
myBinaryTree.insert(90)

# print(myBinaryTree.root.value) # 25

# print(myBinaryTree.root.left.value) #15
# print(myBinaryTree.root.right.value) #50

# print(myBinaryTree.root.left.left.value) #10
# print(myBinaryTree.root.left.right.value) #22
# print(myBinaryTree.root.right.left.value) #35
# print(myBinaryTree.root.right.right.value) #70

# print(myBinaryTree.root.left.left.left.value) #4
# print(myBinaryTree.root.left.left.right.value) #12
# print(myBinaryTree.root.left.right.left.value) #18
# print(myBinaryTree.root.left.right.right.value) #24

# print(myBinaryTree.root.right.left.left.value) #31
# print(myBinaryTree.root.right.left.right.value) #44
# print(myBinaryTree.root.right.right.left.value) #66
# print(myBinaryTree.root.right.right.right.value) #90

# print()
# print("In Order Traversal : ")
# myBinaryTree.traverseInOrder(node=myBinaryTree.root)
# print()
# print("Pre Order Traversal : ")
# myBinaryTree.traversePreOrder(node=myBinaryTree.root)
# print()
# print("Post Order Traversal : ")
# myBinaryTree.traversePostOrder(node=myBinaryTree.root)
# print()

# print(myBinaryTree.lookUp(123)) #False
# print(myBinaryTree.lookUp(35)) #True
# print(myBinaryTree.lookUp(69)) #False
# print(myBinaryTree.lookUp(100)) #Flase
# print(myBinaryTree.lookUp(4)) #True
# print(myBinaryTree.lookUp(18)) #True

myBinaryTree.remove(90)
myBinaryTree.remove(70)