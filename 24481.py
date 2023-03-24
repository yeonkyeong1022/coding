from sys import stdin, setrecursionlimit

N, M, R = map(int, stdin.readline().split())
visited = [False]*(N+1)
graph = [[] for i in range(N+1)]
result = [-1]*(N+1)
setrecursionlimit(N+10)
for i in range(M):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

def dfs(graph, visited, start, count):
    visited[start] = True 
    result[start] = count 
    for i in graph[start]:
        if visited[i] == False:
            dfs(graph, visited, i, count+1)

dfs(graph, visited, R, 0)

for i in range(1, N+1):
    print(result[i])