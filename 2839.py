from sys import stdin 

N = int(stdin.readline())
fiveCnt = N//5
threeCnt = 0
Three = 0
temp = N%5

for i in range(N//5+1):
    if temp %3 == 0:
        threeCnt += (temp//3)
        temp = 0
        break 
    else :
        fiveCnt -=1
        temp +=5
    
if temp != 0:
    print(-1)
else:
    print(fiveCnt+threeCnt)