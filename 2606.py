from sys import stdin, setrecursionlimit

V = int(stdin.readline())
E = int(stdin.readline())
graph = [[] for i in range(V+1)]
visited = [0]*(V+1)
setrecursionlimit(V+10)

for i in range(E):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, visited, start):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(graph, visited, i)

dfs(graph, visited, 1)
print(sum(visited)-1)
