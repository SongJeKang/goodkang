def DFS(core,cnt,num):
    global ans
    global cmp
    global core_num
    if core==core_num:
        if cmp < cnt:
            cmp=cnt
            ans=num
        elif cmp==cnt:
            if ans>num:
                ans=num
        return
    if corelist[core][0]==0 or corelist[core][0]==N-1 or corelist[core][1]==0 or corelist[core][1]==N-1:
        DFS(core+1,cnt+1,num)
        return
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    for i in range(4):
        nx=corelist[core][1]
        ny=corelist[core][0]
        flag=True
        len=0
        while(1):
            nx+=dx[i]
            ny+=dy[i]

            if nx<0 or ny<0 or nx>N-1 or ny>N-1:
                break

            if visit[ny][nx]:
                flag=False
                break
            
            visit[ny][nx]=True
            len+=1
        
        if flag:
            DFS(core+1,cnt+1,len+num)
        while nx-dx[i] != corelist[core][1] or ny-dy[i]!=corelist[core][0]:
            nx-=dx[i]
            ny-=dy[i]
            visit[ny][nx]=False
        
    DFS(core+1,cnt,num)

import sys
input=sys.stdin.readline

Test=int(input())

for t in range(Test):
    core_num=0
    ans=int(1e9)
    cmp=0
    N=int(input())
    graph=[]
    corelist=[]
    visit=[[False]* (N+1) for _ in range(N+1)]
    for i in range(N):
        c= list(map(int,input().split()))
        graph.append(c)

        for j in range(N):
            if graph[i][j]==1:
                corelist.append([i,j])
                visit[i][j]=True
    core_num=len(corelist)
    DFS(0,0,0)
    print("#{}".format(t+1),ans,sep=' ')

    

    
