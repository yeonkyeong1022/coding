from sys import stdin , setrecursionlimit

n = int(stdin.readline())
weight = [[] for i in range(n+1)]
graph = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]

for i in range(n-1):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append([v, w])
    graph[v].append([u, w])
    
setrecursionlimit(n+10)
wSum = 0
ans = []

def dfs(graph, visited, start):
    print(len(graph[start]), start)
    if len(graph[start]) == 1:
        if visited[graph[start][0][0]] == True:
            return True 
    global wSum 
    visited[start] = True
    for i in graph[start]:
        if visited[i[0]] == False:
            wSum += i[1]
            if dfs(graph, visited, i):
                ans.append(wSum)
            visited[i[0]] = False
            wSum -= i[1]
    return False 

for i in range(1, n+1):
    if len(graph[i]) == 1:
        dfs(graph, visited, i)
print(max(ans))