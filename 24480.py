from sys import stdin, setrecursionlimit

N, M, R = map(int, stdin.readline().split())
visited = [False]*(N+1)
graph = [[] for i in range(N+1)]
result = [0]*(N+1)
count = 0
setrecursionlimit(N+10)
for i in range(M):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i] = sorted(graph[i], reverse=True)

def dfs(graph, visited, start):
    global count
    visited[start] = True 
    count+=1
    result[start] = count 
    for i in graph[start]:
        if visited[i] == False:
            dfs(graph, visited, i)

dfs(graph, visited, R)

for i in range(1, N+1):
    print(result[i])