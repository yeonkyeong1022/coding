from sys import stdin, setrecursionlimit 

n = int(stdin.readline())
graph = [[] for _ in range(n+1)]
start, end = map(int, stdin.readline().split())
visited = [False]*(n+1)
setrecursionlimit(n+10)
m = int(stdin.readline())
flag = False 

for i in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, visited, start, depth):
    visited[start] = True
    global flag
    if start == end:
        print(depth)
        flag = True
        return
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, visited, i, depth+1)
dfs(graph, visited, start, 0)
if flag == False:
    print(-1)