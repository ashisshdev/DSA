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



class Node:
    def __init__(self, value=None):
        if(not value):
            self.node = None
        else:
            self.node = {"value": value, "left": None, "right": None}


def traverse(node, translateToJS=False):
    if(node == False or node == None):
        return node

    tree = {"value": node["value"]}
    tree["left"] = None if node["left"] == None else traverse(node["left"])
    tree["right"] = None if node["right"] == None else traverse(node["right"])

    if(not translateToJS):
        return tree
    else:
        return str(tree).replace("None", "null")


class BST:
    def __init__(self):
        newNode = Node()
        self.root = newNode.node

    def insert(self, value):
        newNode = Node(value)

        if(self.root == None):
            self.root = newNode.node
        else:
            currentNode = self.root
            # travells to the leaf node (left or right according to the value)
            while True:
                if(value < currentNode["value"]):
                    if(not currentNode["left"]):
                        currentNode["left"] = newNode.node
                        return
                    currentNode = currentNode["left"]
                else:
                    if(not currentNode["right"]):
                        currentNode["right"] = newNode.node
                        return
                    currentNode = currentNode["right"]

    def lookup(self, value):
        if(not self.root):
            return False
        currentNode = self.root
        while(currentNode):
            if(value < currentNode["value"]):
                currentNode = currentNode["left"]
            elif(value > currentNode["value"]):
                currentNode = currentNode["right"]
            elif(value == currentNode["value"]):
                return currentNode
        return False  # if specified value is not in the node then return False


myTree = BST()

myTree.insert(9)
myTree.insert(4)
myTree.insert(6)
myTree.insert(20)
myTree.insert(170)
myTree.insert(15)
myTree.insert(1)

print(traverse(myTree.root, False))
# print(traverse(myTree.lookup(170), True))
# print(traverse(myTree.lookup(0), True))


#            9
#       4         20
#    1    6    15   170