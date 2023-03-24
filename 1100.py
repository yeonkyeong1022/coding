from sys import stdin 

chess = []

for i in range(8):
    chess.append(list(stdin.readline()))
idx = 0
cnt =0
for i in range(8):
    for j in range(idx, 8, 2):
        if chess[i][j] == 'F':
            cnt += 1
    idx = (idx+1)%2

print(cnt)