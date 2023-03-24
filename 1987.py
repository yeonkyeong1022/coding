from sys import stdin, setrecursionlimit
import copy

R, C = map(int, stdin.readline().split())
board = []
visited = [False]*30
maxD = 0
track = [False]*30

setrecursionlimit(R*C+10)
for i in range(R):
    board.append(list(stdin.readline()))
py = [-1, 1, 0, 0]
px = [0, 0, -1, 1]

def dfs(graph, visited, x, y, d):
    # visited = copy.deepcopy(v)
    visited[ord(graph[x][y])-65] = True
    global maxD
    if maxD <= d :
        maxD = d
    if maxD ==26:
        return
    for i in range(4):
        dx = x+px[i]
        dy = y+py[i]
        if dx<R and dx>=0 and dy<C and dy>=0:
            if visited[ord(graph[dx][dy])-65] == False: 
                dfs(graph, visited, dx, dy, d+1)
                visited[ord(graph[dx][dy])-65] = False
dfs(board, visited, 0, 0, 1)
print(maxD)