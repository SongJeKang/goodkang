import sys
import math
input=sys.stdin.readline

N=int(input())

num=list()
for _ in range(N):
    num.append(int(input()))
num.sort()
divisor=[]
answer=[]
m=num[1]-num[0]
divisor.append(m)
for i in range(2,int(m**(1/2))+1):
    if (m%i==0):
        divisor.append(i)
        if i!=(m//i):
            divisor.append(m//i)
divisor.sort()

for i in divisor:
    cnt=0
    for j in range(1,N):
        if num[j]%i==num[j-1]%i:
            cnt+=1
    
    if cnt==N-1:
        answer.append(i)

print(*answer)