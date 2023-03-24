from sys import stdin, setrecursionlimit

N, M, R = map(int, stdin.readline().split())
visited = [0]*(N+1)
depthh = [-1]*(N+1)
depthh[R] = 0
graph = [[] for i in range(N+1)]
count = 0

for i in range(M):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i] = sorted(graph[i], reverse=True)

setrecursionlimit(N+10)
def dfs(graph, visited, start, depthh, depth):
    global count
    count += 1
    depthh[start] = depth
    visited[start] = count
    for i in graph[start]:
        if depthh[i] == -1 :
            dfs(graph, visited, i,depthh, depth+1)

dfs(graph, visited, R,depthh, 0)
sum = 0
for i in range(1, N+1):
    sum = (sum+visited[i]*depthh[i])
print(sum)