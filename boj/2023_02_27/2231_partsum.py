import sys

input=sys.stdin.readline

N=int(input())

dp=[0 for _ in range(int(1e6)+100)]

for i in range(1,N+1):
    s=str(i)
    sum=i
    for c in s:
        sum+=int(c)

    if dp[sum] ==0:
        dp[sum]=i
    else:
        continue
print(dp[N])
