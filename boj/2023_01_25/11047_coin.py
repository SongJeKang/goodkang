import sys

input=sys.stdin.readline

N,K = map(int,input().split())
coin=list()

for i in range(N):
    coin.append(int(input()))

coin.sort(reverse=True)
ans = 0
for i in range(N):

    if K>=coin[i] and K!=0:
        ans+=K//coin[i]
        K = K % coin[i]

print(ans)