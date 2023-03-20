import sys
from collections import defaultdict
from collections import deque
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def BFS(i):
    queue=deque([i])
    while(queue):
        x=queue.popleft()
        answer.append(x)

        for y in graph[x]:
            if visit[y]==False:
                queue.append(y)
                visit[y]=True

def DFS(i):
    answer.append(i)
    
    for y in graph[i]:
        if visit[y]==False:
            visit[y]=True
            DFS(y)

N,M,Y=map(int,input().split())

visit=[False for _ in range(N+1)]

graph=defaultdict(list)

for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,M+1):
    graph[i].sort()

answer=[]
visit[Y]=True
DFS(Y)
print(*answer)
answer.clear()
visit=[False for _ in range(N+1)]
visit[Y]=True
BFS(Y)
print(*answer)
