import sys

input=sys.stdin.readline

N=int(input())

dp=[0 for _ in range(1001)]
dp[0]=1
dp[1]=1
dp[2]=2
dp[3]=3
dp[4]=5
for i in range(4,N+1):
    dp[i]=dp[i-1]+dp[i-2]
    dp[i]%=10007
print(dp[N])