import sys
input=sys.stdin.readline

N=int(input())

place = list(map(int,input().split()))
dp1 = [0 for i in range(N)]
dp2 = [0 for i in range(N)]
answer=0

for i in range(1,N):
    dp1[i]=dp1[i-1]+place[i]
for i in range(N-2,-1,-1):
    dp2[i]=dp2[i+1]+place[i]
#벌벌꿀
for i in range(1,N):
    answer=max(answer, (dp1[-1]+(dp1[-1]-dp1[i]-place[i])))
#벌꿀벌
for i in range(1,N):
    answer=max(answer, (dp1[-1]+place[i]-place[-1]))
#꿀벌벌
for i in range(N-2,-1,-1):
    answer=max(answer,(dp2[0]+(dp2[0]-dp2[i]-place[i])))
print(answer)
