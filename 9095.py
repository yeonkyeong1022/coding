from sys import stdin 

T = int(stdin.readline())
dynamic = [0]*12
dynamic[2] = 1
for i in range(3, 12):
    if dynamic[i] == 0 :
        for j in range(1,i):
            dynamic[i] = dynamic[i] + dynamic[i-j]+dynamic[j]


for i in range(T):
    n = int(stdin.readline())
    print(dynamic[n])
print(dynamic)