import sys

input=sys.stdin.readline

N,M,B = map(int,input().split())
land=[]
for _ in range(N):
    land.append(list(map(int,input().split())))

m_land=min(map(min,land))                
M_land=max(map(max,land))+1
min_time=int(1e9)
max_height=0

for i in range(m_land,M_land):
    block=0
    cnt=0
    for j in range(N):
        for k in range(M):
            cur=land[j][k]
            if land[j][k] < i:
                cnt+=(cur-i)*(-1)
            else:
                cnt+=(cur-i)*2
            block -= cur-i
    
    if block<=B:
        if cnt<=min_time:
            min_time=cnt
            max_height=i

print(min_time,max_height)
