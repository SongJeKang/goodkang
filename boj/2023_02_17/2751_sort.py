import sys

input=sys.stdin.readline

N=int(input())
mat=[]
for _ in range(N):
    mat.append(int(input()))

mat.sort()

for i in range(N):
    print(mat[i])