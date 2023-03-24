import math 

K = int(input())

length = int(math.log2(K+1))
ans=['4']*length
bina = list(bin(K-(2**length-1)))
idx = length-1

for i in range(len(bina)-1, 1, -1): 
    if bina[i] == '1':
        ans[idx] = '7'
    idx -=1 

A = ''
for i in ans:
    A += i
print(int(A))