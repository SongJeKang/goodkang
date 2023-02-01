import sys

input=sys.stdin.readline

N,M=map(int,input().split())
A=[]
for _ in range(N):
    A.append(int(input()))
A.sort()

tmp=2000000001
if M==0:
    print(0)
    exit(0)
for i in range(N):
    start=i
    end=N-1

    while(start<end):
        mid=(start+end)//2
        if abs(A[i]-A[mid]) >M:
            end=mid
        elif abs(A[i]-A[mid]) ==M:
            print(M)
            exit(0)
        else:
            start=mid+1
    
    if M<=abs(A[i]-A[end]):
        tmp=min(tmp,abs(A[i]-A[end]))

print(tmp)