import sys
input=sys.stdin.readline

N=int(input())
INF=(1e5)
dp=[INF for _ in range(N+1)]

dp[0]=0

for i in range(1,N+1):
    root=int(i**(1/2))
    for j in range(1,root+1):
        dp[i]=min(dp[i],dp[i-j*j]+1)

print(dp[N])
