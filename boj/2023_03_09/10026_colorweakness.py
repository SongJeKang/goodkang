from collections import deque
import sys
def BFS(color,y,x):
    queue=deque()

    queue.append([y,x])

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while(queue):
        cury,curx=queue.popleft()
        for d in range(4):
            nx=curx+dx[d]
            ny=cury+dy[d]

            if 0<=nx<N and 0<=ny<N and visit[ny][nx]==False and grid[ny][nx]==color:
                visit[ny][nx]=True
                queue.append([ny,nx])
                
input=sys.stdin.readline
N=int(input())
visit=[[False for _ in range(N)] for _ in range(N)]
grid=[]

for _ in range(N):
    grid.append(input().strip())
partition=0
partition1=0
for i in range(N):
    for j in range(N):
        if visit[i][j]==False:
            visit[i][j]=True
            color=grid[i][j]
            BFS(color,i,j)
            partition+=1
    
for i in range(N):
    for j in range(N):
        if grid[i][j]=="G":
            grid[i]=grid[i][:j]+'R'+grid[i][j+1:]
            
visit=[[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visit[i][j]==False:
            visit[i][j]=True
            color=grid[i][j]
            BFS(color,i,j)
            partition1+=1

print(partition,partition1)
