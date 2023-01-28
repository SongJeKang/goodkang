import sys

input=sys.stdin.readline

N,M,R=map(int,input().split())
mat=list()
for _ in range(N):
    mat.append(list(map(int,input().split())))

while R>0:
    for i in range(min(N,M)//2):
        x,y=i,i
        now=mat[x][y]
        for j in range(i+1,N-i):
            x=j
            prev,mat[x][y]=mat[x][y],now
            now=prev

        for j in range(i+1,M-i):
            y=j
            prev,mat[x][y]=mat[x][y],now
            now=prev
        
        for j in range(i+1,N-i):
            x=N-j-1
            prev,mat[x][y]=mat[x][y],now
            now=prev

        for j in range(i+1,M-i):
            y=M-j-1
            prev,mat[x][y]=mat[x][y],now
            now=prev
    R-=1

for i in mat:
    print(*i)
