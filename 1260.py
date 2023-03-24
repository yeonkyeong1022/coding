from sys import stdin 
from collections import deque

n, m, v  = map(int, stdin.readline().split())
graph = [[] for i in range(n+1)]
visited = [False]*(n+1) 
for i in range(m):
    v1, v2 = map(int, stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, n+1):
    graph[i] = sorted(graph[i])

def dfs(graph, v, visited):
    visited[v] = True 
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
           dfs(graph, i, visited)

def bfs(graph, start, visited):
    visited[start] = True 
    queue = deque([start])
    print(start, end=' ')
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i] :
                visited[i] = True
                print(i, end= ' ')
                queue.append(i)

dfs(graph, v, visited)
print()
visited = [False]*(n+1) 
bfs(graph, v, visited)