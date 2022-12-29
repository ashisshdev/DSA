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
        
    # if a specific value exists, return true else false
    def lookUp(self,value):
        currentNode = self.root
        while (value):
            if(currentNode.value == value):
                return True 
            elif (currentNode.value > value):
                if(currentNode.left):
                    currentNode = currentNode.left
                else :
                    return False
            else :
                if(currentNode.right):
                    currentNode = currentNode.right
                else :
                    return False
        return False

    def remove(self,value):
        if(self.lookUp(value)):
            pass
        else :
            raise "Element does not exist in the tree."

    # left, root, right
    def traverseInOrder(self, node:Node):
        # transverse through the left half of the tree
        if(node.left):
            self.traverseInOrder(node.left)
        print(node.value , end= ' ')
        if(node.right):
            self.traverseInOrder(node.right)

    # root, left, right
    def traversePreOrder(self,node:Node):
        print(node.value , end=" ")
        if(node.left):
            self.traversePreOrder(node.left)
        if(node.right):
            self.traversePreOrder(node.right)

    # left, right, root 
    def traversePostOrder(self, node:Node):
        if(node.left):  
            self.traversePostOrder(node.left)
        if(node.right):
            self.traversePostOrder(node.right)
        print(node.value , end= ' ')

    # def __repr__(self) -> str:
    #     print(self.root.value)
    #     print(self.root.left)
    #     print(self.root.right)

## Tried to implement remove functionality 
# def remove(root:Node,key):
#    # Base Case
#     if root is None:
#         return root
 
#     # Recursive calls for ancestors of
#     # node to be deleted
#     if key < root.key:
#         root.left = remove(root.left, key)
#         return root
 
#     elif(key > root.key):
#         root.right = remove(root.right, key)
#         return root
 
#     # We reach here when root is the node
#     # to be deleted.
 
#     # If root node is a leaf node
#     if(root.left == None and root.right == None):
#         return None

#     # if there is any one child
#     if(root.left is None):
#         temp = root.right
#         root = None
#         return temp
#     elif(root.right is None):
#         temp = root.left
#         root = None
#         return temp
    
#     # If both children exist

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

print()
print("In Order Traversal : ")
myBinaryTree.traverseInOrder(node=myBinaryTree.root)
print()
print("Pre Order Traversal : ")
myBinaryTree.traversePreOrder(node=myBinaryTree.root)
print()
print("Post Order Traversal : ")
myBinaryTree.traversePostOrder(node=myBinaryTree.root)
print()

print(myBinaryTree.lookUp(123)) #False
print(myBinaryTree.lookUp(35)) #True
print(myBinaryTree.lookUp(69)) #False
print(myBinaryTree.lookUp(100)) #Flase
print(myBinaryTree.lookUp(4)) #True
print(myBinaryTree.lookUp(18)) #True

print(myBinaryTree.remove(100)) #Flase


## Delete method is not implemented in this 

