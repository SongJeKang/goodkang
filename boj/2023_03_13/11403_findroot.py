import sys

input=sys.stdin.readline
N=int(input())
mat=[]

for _ in range(N):
    mat.append(list(map(int,input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if mat[i][j]==0:
                if mat[i][k]==1 and mat[k][j]==1:
                    mat[i][j]=1

for i in range(N):
    print(*mat[i])