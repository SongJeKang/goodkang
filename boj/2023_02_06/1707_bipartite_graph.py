def DFS(k,c):
    global flag
    visit[k] = c
    for next in graph[k]:
        if visit[next]==c:
            flag=False
            return

        if visit[next]==0:
            DFS(next,-c)
    
        
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

Test=int(input())

for _ in range(Test):
    V,E=map(int,input().split())
    flag=True
    graph=[[] for _ in range(V+1)]
    visit=[0]*(V+1)
    for _ in range(E):
        u,v = map(int,input().split())

        graph[u].append(v)
        graph[v].append(u)
    for i in range(V):
        if graph[i] and visit[i]==0:
            DFS(i,1)
    
    if flag:
        print("YES")
    else:
        print("NO")
