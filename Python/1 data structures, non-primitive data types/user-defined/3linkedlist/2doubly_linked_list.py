class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
        self.previous = None 

class DoublyLL:
    def __init__(self,head=None):
        if head is not None:
            node = Node(data=head)
            self.head = node
            self.tail = self.head
            self.length = 1
        else :
            self.head = None
            self.tail = None
            self.length = 0

    def __repr__(self):
        if self.head is not None:
            node = self.head
            nodes = []
            while node is not None:
                nodes.append(node.data)
                node = node.next
            nodes.append("None")
            return " -> <- ".join(str(v) for v in nodes)
        else :
            raise 'Empty Linked List'


    def append(self,data):
        newNode = Node(data=data)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
            self.length+=1
        else :  
            currentTail = self.tail
            self.tail.next = newNode 
            self.tail = newNode 
            self.tail.previous = currentTail
            self.length+=1

    def prepend(self,newData):
        newNode = Node(data=newData)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
            self.length+=1
        else :
            currentHead = self.head
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode
            self.length+=1

    def insert(self,index:int,data):
        if self.head is None or index > self.length:
            raise "Index out of Range"
        else :
            newNode = Node(data=data)
            leaderNode = self.transverseToIndex(index=index-1)
            subsequentNode = leaderNode.next
            newNode.previous = leaderNode
            newNode.next = subsequentNode
            leaderNode.next = newNode
            subsequentNode.previous = newNode
            self.length+=1

    def pop(self):
        if self.tail is None:
            raise "Empty List"
        else :
            lastSecondNode = self.transverseToIndex(index=self.length-2)
            lastSecondNode.next = None 
            self.length-=1 

    def popFirst(self):
        if self.head is None or self.length <= 1:
            raise "Error, cannot operate"
        else:
            secondNode = self.head.next 
            secondNode.previous = None
            self.head = secondNode
            self.length-=1 
    
    def remove(self , index:int):
        if self.head is None or index > self.length:
            raise "Index out of Range"
        else :
            leaderNode = self.transverseToIndex(index=index-1)
            unwantedNode = leaderNode.next
            unwantedNode.next.previous = leaderNode
            leaderNode.next = unwantedNode.next
            self.length-=1
        
    def transverseToIndex(self , index):
        counter = 0
        if self.head is None or index > self.length:
            raise "Index out of bound or empty List !"
        else:
            currentNode = self.head
            while (counter!=index):
                currentNode = currentNode.next
                counter+=1
        return currentNode
        
    def transverse(self):
        if self.head is not None:
            current_node = self.head 
            while current_node is not None:
                yield current_node
                current_node = current_node.next
        else:
            return None
    
    def reverse(self):
        if self.head is not None:
            currentNode = self.head
            previousNode = None
            while (currentNode is not None):
                print(currentNode.data)
                nextNode = currentNode.next
                currentNode.next = previousNode
                currentNode.previous = nextNode 
                previousNode = currentNode
                currentNode = nextNode 
            self.head=previousNode
        else:
            return None

def onelinespace():
    return print()

onelinespace()

# creation
dll = DoublyLL(head=1);
print('list created')
print(f"list length = {dll.length}")
print(f"lenght of dll = {dll.length}")
print(dll)


onelinespace()

# append - add in the end 
print("adding 4 new elements to the dll : ")
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
print(f"lenght of dll = {dll.length}")
print(dll)

onelinespace()

# prepend - adding at the start 
dll.prepend(69)
dll.prepend(70)
dll.prepend(71)
print(f"lenght of dll = {dll.length}")
print(dll)

onelinespace()

# insert - at a specific index
dll.insert(index=5,data=44)
print(f"lenght of dll = {dll.length}")
print(dll)

onelinespace()

# pop - remove the tail element
dll.pop()
print(f"lenght of dll = {dll.length}")
print(dll)

onelinespace()

# popFirst - remove the head element
dll.popFirst()
print(f"lenght of dll = {dll.length}")
print(dll)

onelinespace()

# remove - from a specific index 
dll.remove(3)
print(f"lenght of dll = {dll.length}")
print(dll)

# transverse through the doubly linked list 
for element in dll.transverse():
    if(element.previous is None):
        print("previous = None",end="")
    else:
        print("previous = ",end=str(element.previous.data))
    
    print("     current = ",end=str(element.data))

    if(element.next is None):
        print("     next = None",end="")
    else:
        print("     next = ",end=str(element.next.data))
    print()
