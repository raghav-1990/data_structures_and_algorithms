class Graph:
    def __init__(self, gdict):
        if gdict is None:
            gdict = dict()
        self.gdict = gdict

    def getvertices(self):
        return list(self.gdict.keys())

    def getedges(self):
        edgename = []
        for v in self.gdict:
            for nxtv in self.gdict[v]:
                if {nxtv, v} not in edgename:
                    edgename.append({nxtv, v})
        return edgename
    
    def addvertex(self, vertex):
        if vertex not in self.gdict:
            self.gdict[vertex] = []

    def addedges(self, edge):
        v1, v2 = tuple(set(edge))
        if v1 in self.gdict:
            self.gdict[v1].append(v2)
        else:
            self.gdict[v1] = v2


    
def find_path(graph, start, end, path=[]):
        path = path + [start]
        print(f"the path is now {path}")
        if start == end:
            return path
        if not graph[start]:
            return None
        for node in graph[start]:
            print(f"the node being considerd now is {node}")
            if node not in path:
                newpath = find_path(graph, node, end, path)
                print(f"the newpath is now {newpath}")
                if newpath:
                    return newpath
        return None    

graph_elements = { 
   "a" : ["c","b"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
g = Graph(graph_elements)
print(find_path(g.gdict, 'a', "e", []))
# print(g.getvertices())
# print(g.getedges())