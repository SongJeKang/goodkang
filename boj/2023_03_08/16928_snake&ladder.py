import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
teleport=[0 for _ in range(101)]
visited=[0 for _ in range(101)]
visit=[0 for _ in range(101)]
for _ in range(N+M):
    a,b=map(int,input().split())
    teleport[a]=b
q=deque([1])
visit[1]=1
while 1:
    if visited[100]!=0:
        print(visited[100])
        break

    cur=q.popleft()

    for i in range(1,7):
        next=cur+i
        
        if 1<=next<=100 and visit[next]==0:
            if teleport[next]==0:
                q.append(next)
                visit[next]=1
                visited[next]=visited[cur]+1
            else:
                if visit[teleport[next]]==0:
                    q.append(teleport[next])
                    visit[teleport[next]]=1  
                    visited[teleport[next]]=visited[cur]+1
                else:
                    visit[next]=1
