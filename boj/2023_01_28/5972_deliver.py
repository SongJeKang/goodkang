def dijkstra(k):
    q=[]

    heapq.heappush(q,(0,k))
    cost[k]=0
    while q:
        c,now = heapq.heappop(q)

        if cost[now] < c:
            continue

        for i in graph[now]:
            total=cost[now]+i[1]

            if total < cost[i[0]]:
                cost[i[0]]=total
                heapq.heappush(q,(total,i[0]))


import sys
from collections import defaultdict
import heapq
input=sys.stdin.readline

N,M=map(int,input().split())
INF=int(1e9)
cost=[INF for _ in range(N+1)]
graph=defaultdict(list)

for _ in range(M):
    a,b,c=map(int,input().split())

    graph[a].append([b,c])
    graph[b].append([a,c])

dijkstra(1)

print(cost[N])