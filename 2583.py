from sys import stdin, setrecursionlimit

M, N, K = map(int, stdin.readline().split())

graph = [[0]*M for i in range(N)]

for i in range(K):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            graph[j][k] = 1
setrecursionlimit(N*M+10)
px = [-1, 1, 0, 0]
py = [0, 0, -1, 1]

def dfs(graph, visited, x, y):
    global area 
    area += 1
    visited[x][y] = 1
    graph[x][y] = 1
    for i in range(4):
        dx = x+px[i]
        dy = y+py[i]  
        if 0<= dx and dx<N and 0<= dy and dy<M:
            if graph[dx][dy] == 0:
                dfs(graph, visited, dx, dy)

ans = []
count =0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            area =0 
            visited = [[0]*M for i in range(N)]
            count += 1
            dfs(graph, visited, i, j)
            ans.append(area)
ans.sort()
print(count)
for i in ans:
    print(i, end=' ')