from sys import stdin 
from collections import deque 

N, K = map(int, stdin.readline().split())
visited = [False] *(200000)

def bfs(N, K):
    p = [0]*3
    time = 0
    queue = deque([N])
    while queue:
        time =+1
        x = queue.popleft()
        if x == K:
            return time  
        
        p[0] = x+1
        p[1] = x-1
        p[2] = x*2
        for i in range(3):
            if visited[p[i]] == False:
                visited[p[i]] = True 
                queue.append(p[1])
