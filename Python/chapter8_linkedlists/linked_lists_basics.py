class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

class SinglyLL:
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
            return " -> ".join(str(v) for v in nodes)
        else :
            raise 'Empty Linked List'


    def append(self,data):
        newNode = Node(data=data)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
            self.length+=1
        else :  
            self.tail.next = newNode
            self.tail = newNode
            self.length+=1
            self.transverse()

    def prepend(self,newData):
        newNode = Node(data=newData)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
            self.length+=1
        else :
            newNode.next = self.head
            self.head = newNode
            self.length+=1

    def insert(self,index:int,data):
        if self.head is None or index > self.length:
            raise "Index out of Range"
        else :
            newNode = Node(data=data)
            leaderNode = self.transverseToIndex(index=index-1)
            newNode.next = leaderNode.next
            leaderNode.next = newNode
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
            self.head = secondNode
            self.length-=1
    
    def remove(self , index:int):
        if self.head is None or index > self.length:
            raise "Index out of Range"
        else :
            leaderNode = self.transverseToIndex(index=index-1)
            unwantedNode = leaderNode.next
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
                nextNode = currentNode.next 
                currentNode.next = previousNode
                previousNode = currentNode
                currentNode = nextNode
            self.head=previousNode 
        else:
            return None

def onelinespace():
    return print()

sll = SinglyLL(head=5);
print('list created')
print(f"list length = {sll.length}")
print(sll)
onelinespace()
print("appending 4 new values")
sll.append(6)
sll.append(7)
sll.append(8)
sll.append(9)
print(f"list length = {sll.length}")
print(sll)
onelinespace()
print("prepending 4 new values")
sll.prepend(4)
sll.prepend(3)
sll.prepend(2)
sll.prepend(1)
print(f"list length = {sll.length}")
print(sll)

onelinespace()

print('transversing through list')
for element in sll.transverse():
    print(element.data , end="   ")
print()

onelinespace()

print("popping 1 value")
sll.pop()
print(f"list length = {sll.length}")
print(sll)

onelinespace()

print("popping 1 value - from start")
sll.popFirst()
print(f"list length = {sll.length}")
print(sll)

onelinespace()

print("Inserting 69 at index 3 :")
sll.insert(index=3,data=69)
print(f"list length = {sll.length}")
print(sll)

onelinespace()

print("Removing element at index 6 :")
sll.remove(index=6)
print(f"list length = {sll.length}")
print(sll)

onelinespace()

print("reversing the list")
sll.reverse()
print(sll)
