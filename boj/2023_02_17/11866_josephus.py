import sys

input=sys.stdin.readline

N,K=map(int,input().split())

a=[i for i in range(1,N+1)]
ans=[]
idx=-1
while a:
    idx+=K
    length=len(a)
    if idx < len(a):
        ans.append(a[idx])
        del a[idx]
        idx-=1
    else:
        idx=idx%length
        ans.append(a[idx])
        del a[idx]
        idx-=1

print("<"+", ".join(map(str,ans))+">", sep='')
