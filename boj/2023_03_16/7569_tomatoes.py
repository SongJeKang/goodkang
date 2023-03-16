import sys
from collections import deque
from collections import defaultdict
def BFS(tomatoes):
    cnt=-1
    di=[1,-1,0,0,0,0]
    dy=[0,0,1,-1,0,0]
    dx=[0,0,0,0,1,-1]

    while(queue):
        cnt+=1
        for _ in range(len(queue)):
            i,y,x=queue.popleft()

            for d in range(6):
                ni=i+di[d]
                ny=y+dy[d]
                nx=x+dx[d]

                if 0<= ni < H and 0<= ny < M and 0<=nx<N and mat[ni][ny][nx] ==0:
                    mat[ni][ny][nx]=1
                    queue.append([ni,ny,nx])

    for k in range(H):
        for b in mat[k]:
            if 0 in b:
                return -1
    
    return cnt

input=sys.stdin.readline


N,M,H=map(int,input().split())

mat=defaultdict(list)
queue=deque()
for i in range(H):
    for j in range(M):
        mat[i].append(list(map(int,input().split())))

for i in range(H):
    for j in range(M):
        for k in range(N):
            if mat[i][j][k]==1:
                queue.append([i,j,k])

print(BFS(mat))
