from sys import stdin 
from bisect import bisect_left, bisect_right

N, H = map(int, stdin.readline().split())
obsUp = []
obsDown=[]
for i in range(N):
    obsDown.append(int(stdin.readline()))
    obsUp.append(int(stdin.readline()))

start = 0
end = H
minDisUp = N
minDisDown = N
ans = 0


while start<=end:
    mid = (start+end)//2 
    disObs = 0

    for i in range(N):
        if obsDown <= mid or H-obsUp+1 >= mid:
            disObs += 1
    
    if minObs>disObs:
        minObs = disObs
        ans = minObs
        