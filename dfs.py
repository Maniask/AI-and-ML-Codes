# Program to implement depth for search.
# Created By: Mani Agarwal
# Email : agarwalmani22@gmail.com
# Date  : 20-02-2020
 

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for i in graph[start]:
        if i not in visited:
            dfs(graph, i, visited)
    return visited

graph = {0: [2], 1: [0,2], 2: [3], 3: [1,2]} 
dfs(graph, 1)