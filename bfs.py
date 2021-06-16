import sys, queue

def bfs(adj_list, start):
    visited = {}
    distance = {}
    parent = {}
    for vertex in adj_list:
        visited[vertex] = False
        distance[vertex] = sys.maxsize
        parent[vertex] = None
    distance[start] = 0
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        v = q.get()
        visited[v] = True
        for u in adj_list[v]:
            if not visited[u]:
                distance[u] = distance[v] + 1
                q.put(u)
                parent[u] = v
    print(visited)
    print(distance)
    print(parent)

adj_list = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a'],
    'd': ['b', 'e'],
    'e': ['d']
}
bfs(adj_list, 'a')