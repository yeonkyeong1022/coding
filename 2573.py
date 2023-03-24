from sys import stdin, setrecursionlimit
import copy
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(graph, melt, visited, x, y):
    if x<0 or x>=N or y<0 or y>=M :
        return 
    
    if graph[x][y] == 0:
        return 
    if visited[x][y] == True:
        return 
    visited[x][y] = True

    for i in range(4):
        px = dx[i]+x 
        
        py = dy[i]+y 
        if graph[px][py] == 0:
            melt[x][y] +=1
        dfs(graph, melt, visited, px, py)

    return 

graph = []
N, M = map(int, stdin.readline().split())
setrecursionlimit(N*M+10)
year = 0
count =0 
for i in range(N):
    graph.append(list(map(int, stdin.readline().split())))
allZero = True 
realGraph = []
melt = [[0]*(M) for i in range(N)]
while True:
    count = 0
    allZero = True
    visited = [[False] * M for _ in range(N)]
    for i in range(1, N-1):
        for j in range(1, M-1):
            if graph[i][j] !=0 and visited[i][j] == False:
                dfs(graph,melt, visited, i, j)
                count += 1
    for i in range(1, N-1):
        for j in range(1, M-1):
            graph[i][j] = max(graph[i][j]-melt[i][j], 0)
            if graph[i][j] != 0:
                allZero = False
            melt[i][j] = 0
    
    if(count >= 2):
        print(year)
        break 
    if allZero == True:
        print(0)
        break
    year += 1
    

    
    