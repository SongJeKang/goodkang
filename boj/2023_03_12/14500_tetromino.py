import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
def DFS(i,j,cnt,sum,way):
    global answer

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    if cnt==4:
        answer=max(answer,sum)
        return
    for d in range(4):
        nx=j+dx[d]
        ny=i+dy[d]
            
        if 0<=nx<M and 0<=ny<N and visit[ny][nx] == False and cnt<4:
            visit[ny][nx]=True
            DFS(ny,nx,cnt+1,sum+mat[ny][nx],d)
            visit[ny][nx]=False
            

    if cnt==2:
        if way==0 or way==1:
            if 0<=i-1<N and 0<=i+1<N:
                answer=max(answer,sum+mat[i-1][j]+mat[i+1][j])
        else:
            if 0<=j-1<M and 0<=j+1<M:
                answer=max(answer,sum+mat[i][j-1]+mat[i][j+1])
        
N,M=map(int,input().split())
mat=[]
answer=0

for _ in range(N):
    mat.append(list(map(int,input().split())))
visit=[[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        visit[i][j]=True
        DFS(i,j,1,mat[i][j],0)
        visit[i][j]=False

print(answer)
