def dijkstra(k):
    q=[]

    heapq.heappush(q,(0,k))
    dist[k][k]=0
    while q:
        d,now=heapq.heappop(q)

        if dist[k][now] < d:
            continue

        for i in graph[now]:
            weight=dist[k][now]+i[1]

            if weight < dist[k][i[0]]:
                dist[k][i[0]]=weight
                heapq.heappush(q,(weight,i[0]))


import sys
import heapq
from collections import defaultdict

input=sys.stdin.readline
graph=defaultdict(list)
INF=int(1e9)
N,E=map(int,input().split())
dist=[[INF]*(N+1) for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int,input().split())

    graph[a].append([b,c])
    graph[b].append([a,c])
u,v = map(int,input().split())
dijkstra(1)
dijkstra(u)
dijkstra(v)

first = dist[1][u]+dist[u][v]+dist[v][N]

second = dist[1][v]+dist[v][u]+dist[u][N]

answer = min(first,second)

if answer>= INF:
    print(-1)
else:
    print(answer)