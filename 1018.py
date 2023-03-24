from sys import stdin 

N, M = map(int, stdin.readline().split())
chess = []
color = []

def recolor(x, y, bw):
    cnt=0
    BW = ['B', 'W']
    if bw=='B' : 
        idx = 0
    elif bw=='W' :
        idx = 1

    for i in range(x, x+8):
        for j in range(y, y+8): 
            if BW[idx] != chess[i][j]:
                cnt+=1
            idx = (idx+1)%2
        idx = (idx+1)%2
    return cnt

for i in range(N):
    chess.append(list(stdin.readline().rstrip()))

for i in range(N-7):
    for j in range(M-7):
        color.append(recolor(i, j, 'B'))
        color.append(recolor(i, j, 'W'))
print(min(color))
