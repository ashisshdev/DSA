# For learning purposes we are only creating a simple graph data structure that only supports uni-directional relations i.e. it is directed graph 
# it's also unweighted and asyclic 

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

    def __repr__(self) -> str:
        print(self.adjacencyList)
        for key in self.adjacencyList:
            print(key, '->', self.adjacencyList[key])

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

    myGraph = GraphDataStructure(nodes=someNodes)

    myGraph.addNode(4,[18,19,20])
    myGraph.addNode(5,[23,24])

    myGraph.__repr__()

    myGraph.addVertex(10,99)
    myGraph.addVertex(1,15)

    myGraph.__repr__()

    print(myGraph.getPaths(0,0))
    print(myGraph.getPaths(19,0))
    print(myGraph.getPaths(0,7))
    print(myGraph.getPaths(0,9))

print('\n\n')

#-------------------------------
# practicing again, uncomment to see code and run it for more interactive and understandable implementation because of good examples used

class Graph:
    def __init__(self,nodes) -> None:
        self.nodes = nodes
        self.graphDictionary = {};
        for start,end in self.nodes:
            if start not in self.graphDictionary:
                # if for a starting point there is no ending point the it will create a key in dictionary by name of starting point and add the first occuring ending point in an array for that key in the dictionary
                self.graphDictionary[start] = [end]                 
            else :
                # if the key do exist then it will append the next occuring element directly related to that key 
                self.graphDictionary[start].append(end)
        print(self.graphDictionary)

        # therefore 
        # This 👇
        # [
            # ("Mumbai", "Paris"),
            # ("Mumbai", "Dubai"),
            # ("Paris", "Dubai"),
            # ("Paris", "New York"),
            # ("Dubai", "New York"),
            # ("New York", "Toronto"),
        # ]
        # will become this 👇
        # {
            # 'Mumbai': ['Paris', 'Dubai'], 
            # 'Paris': ['Dubai', 'New York'], 
            # 'Dubai': ['New York'], 
            # 'New York': ['Toronto']
        # }

    # a recursive function that will return all posible paths from one node to another 
    def getPaths(self,start,end,path=[]):

        path = path+[start]

        # base case: if starting and destination are same
        if(start==end):
            return [path]
        # case : if there are no routes from starting point, i.e. it's a leaf node  
        if(start not in self.graphDictionary):
            return []

        paths = []

        # lets start from the starting point and see the available routes 
        for place in self.graphDictionary[start]:
            # if this specific place is not visited
            if place not in path:
                new_paths = self.getPaths(place,end,path)
                for p in new_paths:
                    paths.append(p)
        return paths



if __name__ == '__main__':

    print('operating on international routes :')
    print('1 creation - ')
    internationalRoutes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    # passing array of tuplets 
    internationalRoutesGraph = Graph(
        nodes=internationalRoutes
    )

    print("2 Get paths between two places - ")
    print("2.1 Case 1 : StartingPoint = EndingPoint ")
    start = "Mumbai"
    end = "Mumbai"
    print(f"All paths from {start} to {end} are : \n{internationalRoutesGraph.getPaths(start,end)}")

    print("2.2 Case 2 : StartingPoint is a leaf ")
    start = "Toronto"
    end = "New York"
    print(f"All paths from {start} to {end} are : \n{internationalRoutesGraph.getPaths(start,end)}")

    print("2.3 Case 3 : Ideal scenarion, Mumbai to NewYork ")
    start = "Mumbai"
    end = "New York"
    print(f"All paths from {start} to {end} are : \n{internationalRoutesGraph.getPaths(start,end)}")

    print("2.3 Case 4 : Ideal scenarion 2, Mumbai to Toronto ")
    start = "Mumbai"
    end = "Toronto"
    print(f"All paths from {start} to {end} are : \n{internationalRoutesGraph.getPaths(start,end)}")


    print('\n\n')

    print("operating on local routes :")
    print("1 Cration - ")
    localRoutes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]
    # passing array of tuplets 
    localRoutesGraph = Graph(
        nodes=localRoutes
    )

    print("2 Get paths between two places - ")
    print("2.1 Case 1 : StartingPoint = EndingPoint ")
    start = "Chennai"
    end = "Chennai"
    print(f"All paths from {start} to {end} are : \n{localRoutesGraph.getPaths(start,end)}")

    print("2.2 Case 2 : StartingPoint is a leaf ")
    start = "Bangaluru"
    end = "New York"
    print(f"All paths from {start} to {end} are : \n{localRoutesGraph.getPaths(start,end)}")

    print("2.3 Case 3 : Ideal scenarion, Mumbai to Hyderabad ")
    start = "Mumbai"
    end = "Hyderabad"
    print(f"All paths from {start} to {end} are : \n{localRoutesGraph.getPaths(start,end)}")

    print("2.3 Case 4 : Ideal scenarion 2, Mumbai to Chennai ")
    start = "Mumbai"
    end = "Chennai"
    print(f"All paths from {start} to {end} are : \n{localRoutesGraph.getPaths(start,end)}")

    print("2.3 Case 5 : Ideal scenarion 3, Pune to Bangaluru ")
    start = "Pune"
    end = "Bangaluru"
    print(f"All paths from {start} to {end} are : \n{localRoutesGraph.getPaths(start,end)}")
