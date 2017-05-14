# -*- coding: utf-8 -*-
import sys

graph1 = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0],
]

graph2 = [
    [0, 10, 10, 0],
    [0, 0, 10, 10],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
]

Ms = ({
    (0, 1): 15, (0, 2): 10, (0, 3): 15, (0, 4): 15,
    (1, 5): 24, (2, 1): 5, (2, 6): 5, (3, 6): 10, (3, 7): 7, (4, 7): 10,
    (5, 8): 4, (5, 6): 5, (5, 9): 15, (6, 7): 5, (6, 9): 15, (7, 9): 15,
    (9, 8): 7, (8, 10): 7, (9, 11): 30, (11, 10): 10, (9, 12): 15,
    (10, 13): 15, (11, 13): 20, (12, 13): 15
})


def dicttoMatrice(dictGraph):
    sommets = set()
    for arret in dictGraph:
        sommets.add(arret[0])
        sommets.add(arret[1])
    numvertex = len(sommets)
    matriceGraph = [[0] * numvertex for i in range(numvertex)]
    for start in range(numvertex):
        for end in range(numvertex):
            if (start, end) in dictGraph:
                matriceGraph[start][end] = dictGraph[(start, end)]
    return matriceGraph



class Queue:
    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def front(self):
        return self.items[-1]

     
class Flow:
    def __init__(self, graph = []):
        self.graph = graph
        self.nodenum = self.GetNodenum()
        self.edgenum = self.GetEdgenum()
        self.maxFlow = 0  # The value of max flow , initialized as 0
        self.parent = [0] * self.nodenum  # Used to store path
        self.rGraph = [[0]*self.nodenum for i in range(self.nodenum)]

    def isOutRange(self, x):
        try :
            if x >= self.nodenum or x <= 0:
                raise  IndexError
        except IndexError:
            print("Index Out of Range!")
             
    def GetNodenum(self):
        self.nodenum = len(self.graph)
        return self.nodenum

    def GetEdgenum(self):
        self.GetNodenum()
        self.edgenum = 0
        for i in range(self.nodenum):
            for j in range(self.nodenum):
                if self.graph[i][j] is not 0:
                    self.edgenum = self.edgenum + 1
        return self.edgenum
             
    def BreadthFirstSearch(self, s, t):
        visited = [0] * self.nodenum
        q = Queue()
        q.push(s)
        visited[s] = 1
        self.parent[s] = -1

        while(not q.empty()):
            u = q.front()
            q.pop()
            for v in range(self.nodenum):
                if visited[v]==0 and self.rGraph[u][v]>0:
                    q.push(v)
                    self.parent[v] = u
                    visited[v] = 1

        if visited[t] == 1:
            return True
        else:
            return False

    def fordFulkerson(self, s, t):
        for u in range(self.nodenum):
            for v in range(self.nodenum):
                self.rGraph[u][v] = self.graph[u][v]
        max_flow = 0
        while(self.BreadthFirstSearch(s, t)):
            path_flow = sys.maxint

            v = t
            while(v != s):
                u = self.parent[v]
                path_flow = min(path_flow, self.rGraph[u][v])
                v = self.parent[v]

            v = t
            while(v != s):
                u = self.parent[v]
                self.rGraph[u][v] = self.rGraph[u][v] - path_flow
                self.rGraph[v][u] = self.rGraph[v][u] + path_flow
                v = self.parent[v]

            max_flow += path_flow
        self.maxFlow = max_flow

if __name__ == "__main__":
    flow = Flow(graph1)
    flow.fordFulkerson(0, 5)
    print flow.maxFlow
    flow2 = Flow(graph2)
    flow2.fordFulkerson(0, 3)
    print flow2.maxFlow
    graph3 = dicttoMatrice(Ms)
    flow3 = Flow(graph3)
    flow3.fordFulkerson(0, 13)
    print "Le flot maximum est " + str(flow3.maxFlow)


