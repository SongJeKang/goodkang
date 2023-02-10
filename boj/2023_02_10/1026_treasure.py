import sys
input=sys.stdin.readline

N=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))

A.sort(reverse=True)
ans=0
while A:
    x=A.pop()

    ans+=x*(max(B))

    B.remove(max(B))

print(ans)

