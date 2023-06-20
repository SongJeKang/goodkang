import sys
from collections import defaultdict
from collections import deque

input=sys.stdin.readline

n,m = map(int,input().split())
mapping = list(list())
visit = [[False for i in range(m)]  for i in range(n)]
cnt = [[-1 for i in range(m)] for j in range(n)]
start = list()
for i in range(n):
    a= list(map(int,input().split()))
    mapping.append(a)
    
    for j in range(m):
        if mapping[i][j]==2:
            start=[i,j]
        if mapping[i][j]==0:
            cnt[i][j] = 0
            
dx=[1,-1,0,0]
dy=[0,0,1,-1]
queue = deque()
queue.append(start)
visit[start[0]][start[1]] = True
cnt[start[0]][start[1]] = 0
while(queue):
    y,x = queue.popleft()
    for dxy in range(4):
        nx = x+dx[dxy]
        ny = y+dy[dxy]
        
        if 0<=nx<m and 0<=ny<n and visit[ny][nx]==False :
            if mapping[ny][nx]==0:
                cnt[ny][nx]=0
                visit[ny][nx]=True
            else:
                visit[ny][nx]=True
                cnt[ny][nx]=cnt[y][x]+1
                queue.append([ny,nx])
            
for i in range(n):
    print(*cnt[i])
