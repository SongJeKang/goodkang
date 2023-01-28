import sys
import math
from collections import defaultdict
input=sys.stdin.readline

N,M=map(int,input().split())

graph=defaultdict(list)
dist=[[math.inf for _ in range(N+1)] for _ in range(N+1)]
visit = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())

    graph[a].append(b)
    dist[a][b]=1
answer=0
for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            dist[i][j]=0
print(dist)
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
            
for i in range(1,N+1):
    cnt=1
    for j in range(1,N+1):
        if i==j:
            continue
        if dist[i][j]==math.inf and dist[j][i]==math.inf:
            cnt=0
            break

    answer+=cnt
print(answer)

# taller=defaultdict(set)
# shorter=defaultdict(set)

# for _ in range(M):
#     a,b=map(int,input().split())
#     taller[a].add(b)
#     shorter[b].add(a)

# for i in range(1,N+1):
#     for x in shorter[i]:
#         taller[x].update(taller[i])
#     for y in taller[i]:
#         shorter[y].update(shorter[i])

# answer=0
# for i in range(1,N+1):
#     if len(taller[i]) + len(shorter[i]) == N-1:
#         answer+=1
# print(answer)
