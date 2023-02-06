def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
import sys
from collections import deque
input=sys.stdin.readline

N=int(input())

M=int(input())

E=[]
parent=[i for i in range(N+1)]
for _ in range(M):
    a,b,c=map(int,input().split())

    E.append([a,b,c])
    
E.sort(key=lambda x : x[2])

ans=0
for u,v,w in E:

    pu=find(u)
    pv=find(v)
    print(u,v)
    print(parent)
    if pu==pv:
        continue

    parent[pv]=pu
    ans+=w
    
print(ans)