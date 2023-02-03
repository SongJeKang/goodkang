# def DFS(y,x):
#     dx=[-1,1,0,0,-1,1,-1,1]
#     dy=[0,0,-1,1,1,1,-1,-1]
#     global flag

#     for i in range(8):
#         nx=x+dx[i]
#         ny=y+dy[i]
        
#         if nx<0 or nx>=M or ny<0 or ny>=N:
#             continue
#         if mat[ny][nx] > mat[y][x]:
#             flag=False
#         if visit[ny][nx]==True:
#             continue

#         if mat[ny][nx]==mat[y][x]:
#             visit[ny][nx]=True
#             DFS(ny,nx)
        
def BFS(y,x):
    q=deque()
    q.append([y,x])
    dx=[-1,1,0,0,-1,1,-1,1]
    dy=[0,0,-1,1,1,1,-1,-1]
    global flag
    while q:
        cy,cx=q.popleft()
        for i in range(8):
            
            nx=cx+dx[i]
            ny=cy+dy[i]
            if nx<0 or nx>=M or ny<0 or ny>=N:
                continue
            if mat[ny][nx] > mat[y][x]:
                flag=False
            if mat[ny][nx] !=mat[y][x]:
                continue
            if visit[ny][nx]==True:
                continue
        
            q.append([ny,nx])
            visit[ny][nx]=True


import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10**8)
N,M=map(int,input().split())
mat=[]
visit=[[False for _ in range(M+1)] for _ in range(N+1)]
for _ in range(N):
    mat.append(list(map(int,input().split())))

answer=0
for i in range(N):
    for j in range(M):
        if visit[i][j]==False:
            flag=True
            visit[i][j]=True
            BFS(i,j)
            if flag:
                answer+=1
print(answer)
