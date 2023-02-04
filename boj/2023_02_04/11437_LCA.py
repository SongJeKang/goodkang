def BFS(x,depth):
    q=deque([x])
    visit[x]=True
    d[x]=depth
    while q:
        t=q.popleft()
        depth+=1
        for i in graph[t]:
            if visit[i]:
                continue
            d[i]=depth
            parent[i]=t
            visit[i]=True
            q.append(i)
        
def LCA(a,b):
    while d[a] !=d[b]:
        if d[a] > d[b]:
            a=parent[a]
        else:
            b=parent[b]
    while a!=b:
        a=parent[a]
        b=parent[b]
    return a
import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
graph=[[] for _ in range(N+1)]
parent=[0] * (N+1)
d=[0] *(N+1)
visit=[False] * (N+1)
for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

BFS(1,0)
M=int(input())
for _ in range(M):
    u,v=map(int,input().split())
    print(LCA(u,v))
