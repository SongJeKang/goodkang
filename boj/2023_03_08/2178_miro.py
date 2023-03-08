import sys
from collections import deque
input=sys.stdin.readline
def BFS(i,j,cnt):
    global answer
    queue=deque()

    queue.append([i,j,cnt])
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while queue:
        y,x,c=queue.popleft()
        
        if y==N-1 and x==M-1:
            answer=min(answer,c)
            
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]

            if 0<=nx<M and 0<=ny<N and visit[ny][nx]==False and mat[ny][nx]=='1':
                queue.append([ny,nx,c+1])
                visit[ny][nx]=True


N,M=map(int,input().split())
answer=N*M
visit=[[False for _ in range(M)]for _ in range(N)]
mat=[]
for _ in range(N):
    mat.append(input().strip())

BFS(0,0,1)
print(answer)