# in this implementation of graphs we will implement the bfs and dfs functions 

class GraphDataStructure():
    def __init__(self , nodes = []) -> None: 
        self.adjacencyList = {}
        if len(nodes) :
            for start,end in nodes:
                if(start not in self.adjacencyList):
                    self.adjacencyList[start] = [end]
                else:
                    self.adjacencyList[start].append(end)
        print(self.adjacencyList)

    # add new elements
    def addNode(self,node,childs=[]):        
        if node not in self.adjacencyList:
            self.adjacencyList[node] = childs
        else:
            self.adjacencyList[node].extend(childs)
        # we have to do this extend here else new childs will replace old ones if we use 
        # self.adjacencyList[node] = childs
    
    def addVertex(self , initialNode,targetNode):
        self.adjacencyList[initialNode].extend([targetNode])
    
    def __repr__(self) -> str:
        print(self.adjacencyList)
        for key in self.adjacencyList:
            print(key, '->', self.adjacencyList[key])


    # returns a list of all the possible paths from one point to another 
    def getPaths(self,initialNode,targetNode,path=[]):

        path = path+[initialNode]

        if(initialNode == targetNode):
            return [path]

        if(initialNode not in self.adjacencyList):
            return []
        
        allPaths = []

        for element in self.adjacencyList[initialNode]:
            if element not in path:
                new_paths = self.getPaths(initialNode=element,targetNode=targetNode,path=path)
                for p in new_paths:
                    allPaths.append(p)
        return allPaths

    def breadthTraversal(self,node):
        if(node is None):
            return []

        # here we can utilise a queue to get O(1) operations - using a list for quick implementation
        queue = [node]
        finalQueue = []

        while(len(queue) > 0):
            current_node = queue.pop(0)
            finalQueue.append(current_node)
            if(current_node in self.adjacencyList.keys()):
                for child in self.adjacencyList[current_node]:
                    queue.append(child)
        return finalQueue

    # same thing as above but with less code : 
    # def breadthTraversal(self,node):
    #     stack = [node]
    #     visited = []
    #     while stack:
    #         current = stack.pop(0)
    #         if(current not in visited):
    #             if(current in self.adjacencyList.keys()):
    #                 visited.append(current)
    #                 stack.extend(self.adjacencyList[current])
    #             else:
    #                 visited.append(current)    
    #     return visited

    

    def breadthTraversalWithRecursion(self,queue,finalList):
        if(len(queue)):
            currentNode = queue.pop(0)
            finalList.append(currentNode)
            if(currentNode in self.adjacencyList.keys()):
                for child in self.adjacencyList[currentNode]:
                    queue.append(child)
                return self.breadthTraversalWithRecursion(queue,finalList)
            else:
                return self.breadthTraversalWithRecursion(queue,finalList)
        else: return finalList

    # def depthTraversal(self,node,visited=[]):
    #     if(node not in visited):
    #         visited.append(node)
    #         print(node , end=" ")
    # #        print(self.adjacencyList[node]) 
    #         # if(node in self.adjacencyList.keys()):
    #         for item in self.adjacencyList[node]:
    #             if(item not in visited):
    #                 return self.depthTraversal(node=item,visited=visited)
    #     else : return 

    # def depthTraversal(self,node):
    #     stack = [node]
    #     visited = []
    #     while stack:
    #         current = stack.pop(0)
    #         if(current not in visited):
    #             if(current in self.adjacencyList.keys()):
    #                 visited.append(current)
    #                 stack.extend(self.adjacencyList[current])
    #             else:
    #                 visited.append(current)    
    #     return visited

    def depthTraversal(self,node , visited=[]):
        if(node not in visited):
            visited.append(node)
            if(node in self.adjacencyList.keys()):
                # stack.extend(self.adjacencyList[current])
                for item in self.adjacencyList[node]:
                    return self.depthTraversal(item,visited)
        else: return 

if __name__ == '__main__':
    someNodes = [
        (0,1),
        (1,2),
        (1,3),
        (2,4),
        (2,5),
        (3,6),
        (5,7),
        (5,8),
        (6,9),
        (10,11)
    ]

    print("creating Graph object and passing some initial nodes - ")
    myGraph = GraphDataStructure(nodes=someNodes)

    myGraph.__repr__()

    print("adding nodes 4 and 5 and some children to them - \n(if nodes already exist the children will be added to previous children)")
    myGraph.addNode(4,[18,19,20])
    myGraph.addNode(5,[23,24])

    print("adding vertex between 10,99 and 1,15 - ")
    myGraph.addVertex(10,99)
    myGraph.addVertex(1,15)

    myGraph.__repr__()

    print("getting paths between different nodes:")
    print("1 paths between 0 and 0:")
    print(myGraph.getPaths(0,0))
    print("2 paths between 19 and 0:")
    print(myGraph.getPaths(19,0))
    print("3 paths between 0 and 7:")
    print(myGraph.getPaths(0,7))
    print("4 paths between 0 and 9:")
    print(myGraph.getPaths(0,9))

    print('\n')

    print("traversals : ")
    print("Breadth First Traversals : ")
    print(myGraph.breadthTraversal(node=0))
    print(myGraph.breadthTraversalWithRecursion(queue=[0],finalList=[]))
    print(myGraph.breadthTraversal(node=2))
    print(myGraph.breadthTraversalWithRecursion(queue=[10],finalList=[]))

    myGraph.__repr__()

    print("Depth First Traversals : ")
    print(myGraph.depthTraversal(0))

    print('\n')



