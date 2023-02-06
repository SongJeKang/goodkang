import sys

input=sys.stdin.readline

N=int(input())

dp=[0,0,1,1]
ans=[[0],[1],[2,1],[3,1]]
for i in range(4,N+1):
    dp.append(dp[i-1]+1)
    ans.append(list(ans[i-1])+[i])
    if i%2 ==0:
        if dp[i] > dp[i//2]+1:
            ans[i]=list(ans[i//2]+[i])
            dp[i]=dp[i//2]+1
    if i%3==0:
        if dp[i] > dp[i//3]+1:
            ans[i]=list(ans[i//3]+[i])
            dp[i]=dp[i//3]+1
            
print(dp[N])
ans[N].sort(reverse=True)
print(*ans[N])