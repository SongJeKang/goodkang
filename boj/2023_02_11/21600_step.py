import sys

input=sys.stdin.readline

N=int(input())

histogram=list(map(int,input().split()))
M=0
cmp=0
for i in range(N):
    if histogram[i] > cmp:
        cmp+=1
    else:
        cmp=histogram[i]

    M=max(M,cmp)
print(M)
