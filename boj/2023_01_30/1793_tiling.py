import sys
input=sys.stdin.readline

answer=[]
dp=[0 for _ in range(251)]
dp[0],dp[1]=1,1

while True:
    try:
        n=int(input())
        
        for i in range(2,n+1):
            dp[i]=dp[i-2]*2+dp[i-1]
        
        answer.append(dp[n])

    except:
        for i in answer:
            print(i)
        break
