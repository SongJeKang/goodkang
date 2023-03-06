import sys
input=sys.stdin.readline

N=int(input())

lst=list(map(int,input().split()))

lst.sort()

dp=[0 for _ in range(N)]
dp[0]=lst[0]

for i in range(1,N):
    dp[i]=dp[i-1]+lst[i]

print(sum(dp))