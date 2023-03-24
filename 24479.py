from sys import stdin, setrecursionlimit

def main():
        
    N, M, R = map(int, stdin.readline().split())
    graph = [[] for i in range(N+1)]
    result = [0]*(N+1)
    visited = [False]*(N+1)
    count=0
    setrecursionlimit(N+10)
    for i in range(M):
        u, v = map(int, stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(N+1):
        graph[i] = sorted(graph[i], reverse=True)

    def dfs(graph, start, visited):
        nonlocal result
        nonlocal count
        count+=1
        visited[start] = True 
        result[start] = count
        for i in graph[start]:
            if not visited[i]:
                dfs(graph, i, visited) 
            

    dfs(graph, R, visited)

    for i in range(1, N+1):
        print(result[i])

main()