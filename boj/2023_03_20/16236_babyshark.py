import sys
input=sys.stdin.readline
from collections import deque

def BFS(i,j,level):
    queue=deque()
    queue.append([i,j,0])
    tmp=[]
    while(queue):
        y,x,c=queue.popleft()
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
    
        for d in range(4):
            nx=dx[d]+x
            ny=dy[d]+y

            if 0<=nx<N and 0<=ny<N and visit[ny][nx]==False and mat[ny][nx]<=level:
                if mat[ny][nx] !=0 and mat[ny][nx]<level:
                    tmp.append([ny,nx,c+1])
                    queue.append([ny,nx,c+1])
                    visit[ny][nx]=True
                else:
                    queue.append([ny,nx,c+1])
                    visit[ny][nx]=True
    
    tmp.sort(key=lambda x: (x[2],x[0],x[1]),reverse=True)
    return tmp

        
N=int(input())
mat =[]
shark=[]
level=2
for i in range(N):
    mat.append(list(map(int,input().split())))

    for j in range(len(mat[i])):
        if mat[i][j]==9:
            mat[i][j]=0
            shark=[i,j]

a=list()
time=0
exp=0
while 1:
    if exp==level:
        level+=1
        exp=0
    visit=[[False for _ in range(N)] for _ in range(N)]
    a=BFS(shark[0],shark[1],level)
    if a:
        i,j,d=a.pop()
        exp+=1
        time+=d
        shark[0]=i
        shark[1]=j

        mat[i][j]=0
    else:
        print(time)
        break
        

