def bfs(k):
    global m
    global cnt
    q=[]
    heapq.heappush(q,(stone[k],k))

    while(q):
        st,cur=heapq.heappop(q)
        for i in room[cur]:
            
            if visit[i] == False:
                visit[i]=True
                heapq.heappush(q,(stone[i],i))
                cnt+=1
        m=min(m,st)

import sys
import heapq

input=sys.stdin.readline

N,M,K=map(int,input().split())

stone = list(map(int,input().split()))
room = [[(i-1)%(N),(i+1)%(N)] for i in range(N)]
visit=[False] *(N+1)
for _ in range(M):
    i,j=map(int,input().split())

    room[i-1].remove(j-1)
    room[j-1].remove(i-1)
ans=0
for i in range(N):
    m=int(5e9)
    cnt=1
    if visit[i]==False:
        visit[i]=True
        bfs(i)
        ans+=m
    if cnt==N:
        print("YES")
        exit(0)
if ans>K:
    print("NO")
else:
    print("YES")