from sys import stdin, setrecursionlimit

M, N = map(int, stdin.readline().split())
graph = []
setrecursionlimit(N*M+10)
count = 0
for i in range(M):
    graph.append(list(map(int, stdin.readline().split())))

visited = [0]*(graph[0][0]+1)
px = [0, 0, -1, 1]
py = [-1, 1, 0, 0]
isNoWay = False
noWayNums = [False]*(graph[0][0]+1) 

def dfs(graph, visited, x, y):
    global isNoWay
    height = graph[x][y]
    visited[height]= 1
    global count
    if x == M-1 and y == N-1:
        count += 1
        print()
        return
    elif graph[M-1][N-1] >= height:
        return
    for i in range(4):
        dx = px[i]+x 
        dy = py[i]+y 
        if 0<=dx and dx<M and 0<=dy and dy<N:
            if graph[dx][dy] < height and visited[graph[dx][dy]] == 0 and noWayNums[graph[dx][dy]] == False:
                isNoWay = False
                temp = graph[dx][dy]
                graph[dx][dy] = height
                print(temp, end=' ')
                dfs(graph,visited, dx, dy)
                if isNoWay == False and dx != M-1 and dy!= N-1:
                    print()
                    isNoWay = True
                    noWayNums[temp] = True
                
                visited[temp] = 0
                graph[dx][dy] = temp
print(noWayNums)
dfs(graph,visited, 0, 0)
print(count)