from sys import stdin 
from bisect import bisect_left, bisect_right
from statistics import mode, mean, median

def myMode(arr):
    mmode = 0
    mmode = mode(arr)
    if len(arr)==1:
        return mmode
    modeCnt = bisect_right(arr, mmode)-bisect_left(arr, mmode)
    del arr[bisect_left(arr, mmode):bisect_right(arr, mmode)]
    temp = mode(arr)
    if modeCnt == bisect_right(arr, temp)-bisect_left(arr, temp):
        mmode = temp
    return mmode 

N = int(stdin.readline())
arr = []
sum = 0
for i in range(N):
    arr.append(int(stdin.readline()))
    sum += arr[i]
    
arr.sort()
mmean = mean(arr)
mmedian = median(arr)
minMax = arr[-1]-arr[0]
mmode = myMode(arr)

print(int((mmean+0.5)*10//10))
print(mmedian)
print(mmode)
print(minMax)

    

