import sys
from collections import defaultdict
input=sys.stdin.readline

s=input().strip()
alpa=defaultdict(int)
dp=[0 for _ in range(len(s)+1)]
# for i in range(1,27):
#     alpa[i]=[chr(64+i),0]
if s[0]=="0":
    print(0)
    exit(0)

dp[0]=1
dp[1]=1
for i in range(2,len(s)+1):
    if s[i-1] !="0":
        dp[i]=dp[i]+dp[i-1]

    if 10<=int(s[i-2]+s[i-1])<=26:
        dp[i]=dp[i]+dp[i-2]

print(dp[-1]%1000000)
