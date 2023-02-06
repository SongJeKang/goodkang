# def bfs(k):
#     q=deque([k])
    
#     while q:
#         cur=q.popleft()

#         for next in graph[cur]:
#             if visit[next]==False:
#                 visit[next]=True
#                 root[next].update(root[cur])
#                 q.append(next)

# import sys
# from collections import deque
# from collections import defaultdict
# input=sys.stdin.readline

# N=int(input())
# v=[]
# graph=defaultdict(list)
# root=[{i} for i in range(N+1)]
# visit=[False for _ in range(N+1)]
# for _ in range(N-1):
#     a,b=map(int,input().split())

#     graph[a].append(b)
#     graph[b].append(a)

# bfs(1)
# root[1]={1}

# M=int(input())
# for _ in range(M):
#     answer=0
#     u,v=map(int,input().split())
#     s = root[u].intersection(root[v])

#     m=0

#     for i in s:
#         if m<len(root[i]):
#             m=len(root[i])
#             answer=i

#     print(answer)
def DFS(x,depth):
    visit[x]=True
    d[x]=depth
    for i in graph[x]:
        if visit[i]:
            continue
        parent[i][0]=x
        DFS(i,depth+1)
def setparent():
    for i in range(1,L):
        for j in range(1,N+1):
            parent[j][i]=parent[parent[j][i-1]][i-1]
def LCA(a,b):
    if d[a] > d[b]:
        a,b = b,a
    for i in range(L-1,-1,-1):
        if d[b]-d[a] >= (1<<i):
            b=parent[b][i]
    if a==b:
        return a

    for i in range(L-1,-1,-1):
        if parent[a][i]!=parent[b][i]:
            a=parent[a][i]
            b=parent[b][i]
    return parent[a][0]
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
L=21 #max depth
N=int(input())
graph=[[] for _ in range(N+1)]
parent=[[0]*L for _ in range(N+1)]
d=[0] *(N+1)
visit=[False] * (N+1)
for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

DFS(1,0)
setparent()

M=int(input())
for _ in range(M):
    u,v=map(int,input().split())
    print(LCA(u,v))