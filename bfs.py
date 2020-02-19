# Program to implement breadth for search.
# Created By: Mani Agarwal
# Email : agarwalmani22@gmail.com
# Date  : 20-02-2020

def bfs(graph, root):
    visited, queue = set(), [root]
    visited.add(root)
    while queue: 
        vertex = queue.pop(0)
        print(vertex)
        for neighbour in graph[vertex]: 
            if neighbour not in visited: 
                visited.add(neighbour) 
                queue.append(neighbour) 

graph = {0: [2], 1: [0,2], 2: [3], 3: [1,2]} 
bfs(graph, 2) 