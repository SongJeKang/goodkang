import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(v,cnt):
    if cnt == 5:
        print(1)
        exit(0)
    
    for i in people[v]:
        
        if visit[i]==False:
            visit[i]=True
            DFS(i,cnt+1)
            visit[i]=False
N,M=map(int,input().split())

check=0

people = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    
    people[a].append(b)
    people[b].append(a)

for i in range(N):
    visit= [False for _ in range(N)]
    if len(people[i])==0:
        continue
    
    visit[i]=True
    DFS(i,1)
    visit[i]=False

print(0)