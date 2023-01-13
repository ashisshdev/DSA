# in this implementation of trees we will implement the bfs and dfs functions properly in out custom made tree data structure 

# Copying Trees implementation from data structures 
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
            # TODO
            pass
        else :
            raise "Element does not exist in the tree."


    def breadthTraverse(self,node:Node):
        # root -> next level l2r -> next level l2r -> ...
        ## an array can be requested as a parameter to store elements as they occur

        if(node is None):
            return []

        # here we can utilise a queue to get O(1) operations 
        queue = [node]
        finalQueue = []

        while(len(queue) > 0):
            current_node = queue.pop(0)
            finalQueue.append(current_node.value)
            if(current_node.left):
                queue.append(current_node.left)
            if(current_node.right):
                queue.append(current_node.right)
        
        return finalQueue

    # implementing breadth first traversal but using recursion
    def breadthTraversalWithRecurssio(self,queue,finalList):
        if(len(queue)):
            current_node = queue.pop(0)
            finalList.append(current_node.value)
            if(current_node.left):
                queue.append(current_node.left)
            if(current_node.right):
                queue.append(current_node.right)
            return self.breadthTraversalWithRecurssio(queue,finalList)

        else: return finalList

    # using recursive approach in each variation of depth first search 

    # left, root, right
    def depthTraverseInOrder(self, node:Node , list):
        # transverse through the left half of the tree
        if(node.left):
            self.depthTraverseInOrder(node.left , list)
        list.append(node.value)
#        print(node.value , end= ' ')
        if(node.right):
            self.depthTraverseInOrder(node.right , list)
        return list

    # root, left, right
    def depthTraversePreOrder(self,node:Node , list):
        list.append(node.value)
        if(node.left):
            self.depthTraversePreOrder(node.left , list)
        if(node.right):
            self.depthTraversePreOrder(node.right , list)
        return list

    # left, right, root 
    def depthTraversePostOrder(self, node:Node , list):
        if(node.left):  
            self.depthTraversePostOrder(node.left , list)
        if(node.right):
            self.depthTraversePostOrder(node.right , list)
        list.append(node.value)
        return list

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

# our tree currently looks like this: 
#                       25
#             15                  50
#        10       22          35       70
#      4   12   18  24      31  44   66  90

# Breadth first traversal should look like this : 25   15 50   10 22 35 70    4 12 18 24 31 44 66 90
print(myBinaryTree.breadthTraverse(node=myBinaryTree.root))
print(myBinaryTree.breadthTraversalWithRecurssio([myBinaryTree.root],[]))

#-----------------------
print()


# Depth first search - In Order ,that is, left,root,right : 4 10 12 15 18 22 24 25 31 35 44 50 66 70 90
print(myBinaryTree.depthTraverseInOrder(node=myBinaryTree.root , list=[]))
# > Returns all items of tree in a sorted way

# Depth first search - In Order ,that is, left,root,right : 25 15 10 4 12 22 18 24 50 35 31 44 70 66 90
print(myBinaryTree.depthTraversePreOrder(node=myBinaryTree.root , list=[]))
# > Returns all items of tree in an array which can be used to recreate the tree 

# Depth first search - In Order ,that is, left,root,right : 4 12 10 18 24 22 15 31 44 35 66 90 70 50 25  
print(myBinaryTree.depthTraversePostOrder(node=myBinaryTree.root , list=[]))
# > useful to delete tree (delete all value above 70 , the moment we reach right of seventy we drop everything and point it to null)

