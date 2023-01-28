import sys
import math
input=sys.stdin.readline

N,M=map(int,input().split())
dist=[[math.inf for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())

    dist[a][b]=1
    dist[b][a]=1

for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            dist[i][j]=0

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
print(dist)
m=math.inf
answer=0
for i in range(1,N+1):
    if sum(dist[i][1:]) < m:
        m=sum(dist[i][1:])
        answer=i

print(answer)
