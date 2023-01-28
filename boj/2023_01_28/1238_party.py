def dikstra(k):
    q=[]

    heapq.heappush(q,(0,k))
    dist[k][k]=0
    while q:
        t,now=heapq.heappop(q)
        if dist[k][now] < t:
            continue

        for x in graph[now]:
            time = dist[k][now]+x[1]

            if time < dist[k][x[0]]:
                dist[k][x[0]]=time
                heapq.heappush(q,(time,x[0]))


import heapq
import sys
from collections import defaultdict


input=sys.stdin.readline

N,M,X = map(int,input().split())
graph = defaultdict(list)
INF=int(1e9)
dist = [[INF for _ in range(N+1)]for _ in range(N+1)]
for _ in range(M):
    a,b,t=map(int,input().split())
    graph[a].append([b,t])
for i in range(1,N+1):
    dikstra(i)

answer=0
for i in range(1,N+1):
    cnt = dist[i][X] + dist[X][i]
    
    answer=max(cnt,answer)
print(answer)