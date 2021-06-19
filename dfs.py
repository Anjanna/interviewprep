import sys

class DFS:
    def __init__(self, adj_list = None):
        self.adj_list = adj_list
        self.parent = {}
        self.distance = {}
        self.time = 0
        self.color = {}

    def dfs(self):
        for vertex in self.adj_list:
            self.color[vertex] = "white"
            self.distance[vertex] = sys.maxsize
            self.parent[vertex] = None
        for vertex in self.adj_list:
            self.dfs_helper(vertex)
        print(self.color)
        print(self.distance)
        print(self.parent)

    def dfs_helper(self, vertex):
        self.time += 1
        self.distance[vertex] = self.time
        self.color[vertex] = "gray"
        for u in self.adj_list[vertex]:
            if self.color[u] == "white":
                self.parent[u] = vertex
                self.dfs_helper(u)
        self.time += 1
        self.color[vertex] = "black"

adj_list = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a'],
    'd': ['b', 'e'],
    'e': ['d']
}
d = DFS(adj_list)
d.dfs()