import sys

input=sys.stdin.readline

N=int(input())
P=list(map(int,input().split()))

dp=[0]+P

for i in range(N+1):
    for j in range(1,i):
        dp[i]=max(dp[i],dp[i-j]+P[j-1])

print(dp[-1])