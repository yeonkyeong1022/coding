from sys import stdin, setrecursionlimit
import copy

N = int(stdin.readline())
graph = []
maxH = 0
minH = 100
for i in range(N):
    graph.append(list(map(int, stdin.readline().split())))
    if maxH < max(graph[i]):
        maxH = max(graph[i])
    if minH >min(graph[i]):
        minH = min(graph[i])
px = [-1, 1, 0, 0]
py = [0, 0, -1, 1]
setrecursionlimit(N*N+10)
def dfs(graph, x, y, height):
    graph[x][y] = height-1
    for i in range(4):
        dx = x+px[i]
        dy = y+py[i]
        if dx<N and dx>=0 and dy<N and dy>=0:
            if graph[dx][dy] > height:
                dfs(graph, dx, dy, height)
maxArea = 0
copyList = []
ansH =0 
AA = []
for height in range(minH-1, maxH+1):
    Area = 0
    copyList = copy.deepcopy(graph)
    for j in range(N):
        for k in range(N):
            if copyList[j][k] > height:
                Area += 1
                dfs(copyList, j, k, height) 
    # if maxArea < Area :
    #     maxArea = Area
    #     ansH = height
    AA.append(Area)
print(max(AA))