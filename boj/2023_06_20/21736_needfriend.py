import sys
input =sys.stdin.readline
from collections import deque

campus = list(list())
N,M = map(int,input().split())

visit = [[False for i in range(M)] for j in range(N)]
start=list()
queue = deque()
cnt=0

for i in range(N):
    a=input().strip()
    campus.append(a)
    
    for j in range(M):
        if a[j]=="I":
          start.append([i,j])  
    
dx = [1,-1,0,0]
dy = [0,0,1,-1]

visit[start[0][0]][start[0][1]]=True
queue.append(start[0])

while(queue):
    y,x = queue.popleft()
    for dxy in range(4):
        nx = x+dx[dxy]
        ny = y+dy[dxy]
        
        if 0<=nx<M and 0<=ny<N and visit[ny][nx]==False and campus[ny][nx] !='X':
            visit[ny][nx]=True
            queue.append([ny,nx])
            if campus[ny][nx]=='P':
                cnt+=1


if cnt==0:
    print("TT")
else:
    print(cnt)
    