import sys

input=sys.stdin.readline
N=int(input())
X=list(map(int,input().split()))
dp=[0 for _ in range(N)]
s=[]

for i in range(N):
    s.append([i,X[i]])

s.sort(key=lambda x:x[1])
idx=0
dp[s[0][0]]=0
for i in range(1,N):
    if s[i][1]==s[i-1][1]:
        dp[s[i][0]]=idx
    else:
        idx+=1
        dp[s[i][0]]=idx

print(dp)
