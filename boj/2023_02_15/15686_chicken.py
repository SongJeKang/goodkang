def DFS(ck,cnt):
    global M
    global ck_num
    global ans
    distance=0
    memo=[]
    if cnt>M:
        return
    if ck==ck_num:
        if cnt<=M:
            for x in house:
                distance+=x[2]
            
            ans=min(ans,distance)
        return

    for x in house:
        memo.append(x[2])
        if x[2]>abs(chicken[ck][0]-x[0])+abs(chicken[ck][1]-x[1]):
            x[2]=abs(chicken[ck][0]-x[0])+abs(chicken[ck][1]-x[1])
    DFS(ck+1,cnt+1)

    for i in range(len(memo)):
        house[i][2]=memo[i]
    
    DFS(ck+1,cnt)
    
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

N,M=map(int,input().split())

mat=[]
chicken=[]
house=[]
ans=int(1e9)
cmp=0
for i in range(N):
    mat.append(list(map(int,input().split())))

    for j in range(N):
        if mat[i][j]==2:
            chicken.append([i,j])
        elif mat[i][j]==1:
            house.append([i,j,N*N])
ck_num=len(chicken)
DFS(0,0)


print(ans)