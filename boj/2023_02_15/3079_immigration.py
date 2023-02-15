import sys
input=sys.stdin.readline

N,M=map(int,input().split())
time=[]
for _ in range(N):
    time.append(int(input()))

time.sort()

start=0
end=int(1e18)
answer=int(1e18)
while(start<=end):
    total=0

    mid=(start+end)//2

    for i in time:
        total+=mid//i

    if total>=M:
        answer=min(answer,mid)
        end=mid-1
    else:
        start=mid+1
print(answer)