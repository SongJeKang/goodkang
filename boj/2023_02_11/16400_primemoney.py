import sys
input=sys.stdin.readline

N=int(input())

flag=[False,False]+[True]*(N+1)
prime=[]
for i in range(2,N+1):
    if flag[i]:
        prime.append(i)
        for j in range(2*i,N+1,i):
            flag[j]=False

dp=[0 for _ in range(N+1)]
dp[0]=1
for i in prime:
    for j in range(i,N+1):
        dp[j]+=dp[j-i]
    
    dp[j]=dp[j]%123456789
print(dp[N])