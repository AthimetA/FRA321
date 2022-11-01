import os

class Graph:
    def __init__(self, name, path, cost, depth , dataPath = 'data.txt'):
        self.citiesAndPaths = self.GetCitiesGraph(dataPath)
        self.name = name
        self.path = path
        self.cost = cost
        self.depth = depth
    
    def GetCitiesGraph(self,dataPath):
        dictGraph = {}
        path = os.path.dirname(os.path.abspath(__file__))
        dataPath = os.path.join(path, dataPath)
        with open(dataPath, 'r') as f:
            for line in f:
                cityA, cityB, cost = line.strip().split(' ')
                cost = int(cost)
                if cityA not in dictGraph:
                    dictGraph[cityA] = {cityB: cost}
                else:
                    dictGraph[cityA][cityB] = cost
                if cityB not in dictGraph:
                    dictGraph[cityB] = {cityA: cost}
                else:
                    dictGraph[cityB][cityA] = cost
        return dictGraph

class AgentNode(Graph):
    def __init__(self, name, path, cost, depth, dataPath = 'data.txt'):
        super().__init__(name, path, cost, depth, dataPath)
        self.children = []