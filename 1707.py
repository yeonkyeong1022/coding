from sys import stdin, setrecursionlimit 

def dfs(graph, visited, flags, start, flag):
    visited[start] = True 
    flags[start] = flag
    for i in graph[start]:
        if visited[i] == False:
            if flag == True :
                dfs(graph, visited, flags, i, False)
            else :
                dfs(graph, visited, flags, i, True)
K = int(stdin.readline())
ans = "YES"
for i in range(K):
    V, E = map(int, stdin.readline().split())
    setrecursionlimit(V+10)
    flags = [False]*(V+1)
    graph = [[] for i in range(V+1)]
    visited = [False]*(V+1)
    for j in range(E):
        u, v = map(int, stdin.readline().split())
        graph[v].append(u)
        graph[u].append(v)
    
    for j in range(1, V+1):
        if visited[j] == False:
            dfs(graph, visited, flags, j, True)
    
    for j in range(1, V+1):
        for k in graph[j]:
            if flags[k] == flags[j] :
                ans = "NO"
                break

    print(ans)
