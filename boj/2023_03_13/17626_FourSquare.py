import sys

input=sys.stdin.readline
N=int(input())
dp=[0 for _ in range(N+1)]
Maxidx=int(N**(1/2))
for i in range(Maxidx+1):
    dp[i**2]=1
end=int((N-1)**(1/2))
for i in range(1,N):
    for j in range(1,end+1):
        if (i+j**2) <=N:
            if dp[i+j**2] !=0:
                dp[i+j**2]=min(dp[i+j**2],dp[i]+1)
            else:
                dp[i+j**2]=dp[i]+1
        else:
            break

print(dp[N])