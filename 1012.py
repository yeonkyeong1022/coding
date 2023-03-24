from sys import stdin, setrecursionlimit


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(stdin.readline())
for t in range(T):
    count = 0
    M, N, K = map(int, stdin.readline().split())
    graph = [[0]*N for i in range(M)]
    setrecursionlimit(M*N+10)
    for i in range(K):
        px, py = map(int, stdin.readline().split())
        graph[px][py] = 1

    def dfs(graph, x, y):
        for i in range(4):
            if x+dx[i] < M and x+dx[i]>=0 and y+dy[i]<N and y+dy[i]>=0:
                if graph[x+dx[i]][y+dy[i]] ==1:
                    graph[x+dx[i]][y+dy[i]] = 2
                    dfs(graph, x+dx[i], y+dy[i])   

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                count += 1
                dfs(graph, i, j)
    print(count)