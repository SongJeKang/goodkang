import sys

input=sys.stdin.readline

N=int(input())

dp=[0 for _ in range(N+1)]

dp[0]=3
dp[1]=7

for i in range(2,N+1):
    dp[i]=(dp[i-1]*2+dp[i-2])%9901

print(dp[N-1])