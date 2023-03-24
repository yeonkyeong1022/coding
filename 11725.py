from sys import stdin, setrecursionlimit

N = int(stdin.readline())
graph = [[] for i in range(N+1)]
visited = [False]*(N+1)
parentT = [0]*(N+1)
setrecursionlimit(N+10)

for i in range(N-1):
    u, v = map(int,stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, visited, parentT, start):
    visited[start] = True 
    for i in graph[start]:
        if visited[i] ==False:
            parentT[i] = start
            dfs(graph, visited, parentT, i)

dfs(graph, visited, parentT, 1)
for i in range(2, N+1):
    print(parentT[i])