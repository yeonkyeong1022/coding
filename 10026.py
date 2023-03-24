from sys import stdin, setrecursionlimit

N = int(stdin.readline())
graph = []
px = [-1, 1, 0, 0]
py = [0, 0, -1, 1]
color_count = 0
non_color_count = 0
setrecursionlimit(N*N+10)
for i in range(N):
    graph.append(list(stdin.readline().rstrip()))

def dfs_non_color(graph, x, y, RGB):
    color = graph[x][y]
    for i in range(4):
        dx = x+px[i]
        dy = y+py[i]
        if dx<N and dx>=0 and dy<N and dy>=0:
            if (graph[dx][dy] == 'r' or graph[dx][dy] == 'g') and RGB == 'y':
                graph[dx][dy] = 'y'
                dfs_non_color(graph, dx, dy, 'y')
            elif graph[dx][dy] == 'b'and RGB == 'b':
                graph[dx][dy] = 'B'
                dfs_non_color(graph, dx, dy, 'b')

def dfs_color(graph, x, y):
    color = graph[x][y]
    graph[x][y] = color.lower()
    for i in range(4):
        dx = x+px[i]
        dy = y+py[i]
        if dx<N and dx>=0 and dy<N and dy>=0:
            if graph[dx][dy] == color.upper():
                graph[dx][dy] = color.lower()
                dfs_color(graph, dx, dy)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R' or graph[i][j] == 'G' or graph[i][j] == 'B':
            color_count+=1
            dfs_color(graph, i, j)
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'r' or graph[i][j] == 'g':
            non_color_count += 1
            dfs_non_color(graph, i, j, 'y')
        elif graph[i][j] == 'b':
            non_color_count += 1
            dfs_non_color(graph, i, j, 'b')

print(color_count, non_color_count)