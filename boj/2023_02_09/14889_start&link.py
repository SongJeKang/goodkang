# def DFS(k,cnt,val):
#     if cnt

#     for i in range(N):
#         if index[i]!=i and visit[i]==False:
#             val+=mat[k][i]+mat[i][k]
#             DFS(i,cnt+1,val)
import sys
from itertools import combinations
input=sys.stdin.readline

N=int(input())
mat=list()
num=N//2
index=[i for i in range(N)]
for _ in range(N):
    mat.append(list(map(int,input().split())))
ans=10001
for i in combinations(index,num):
    sum1=0
    sum2=0
    part2=set(index)
    for j in i:
        part2.remove(j)
    if i[0]==num+1:
        break
    i=list(i)
    part2=list(part2)
    for x in range(len(part2)):
        for y in range(x,len(part2)):
            if part2[x]!=part2[y]:
                sum1 += mat[part2[x]][part2[y]]+mat[part2[y]][part2[x]]
    for x in range(len(i)):
        for y in range(x,len(i)):
            if i[x]!=i[y]:
                sum2+=mat[i[x]][i[y]]+mat[i[y]][i[x]]

    ans=min(ans,abs(sum2-sum1))

print(ans)