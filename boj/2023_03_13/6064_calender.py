import sys
input=sys.stdin.readline

Test=int(input())
dp=[i for i in range(40001)]
for _ in range(Test):
    M,N,x,y=map(int,input().split())

    
    diff=abs(M-N)
    seq=set()
    seq_lst=[]
    Maxidx=0
    cnt=0
    answer=0
    if M == 1 or N==1:
        print(max(x,y))
        continue
    if M<N:
        if N%diff==0:
            Maxidx=(N//diff)
        else:
            Maxidx=(N)
        idx=x
        for _ in range(Maxidx):

            if dp[idx]!=y:
                cnt+=1
            else:
                answer=x+M*cnt
                break

            idx-=diff
            
            if idx<=0:
                idx=N-abs(idx)
        if answer==0:
            print(-1)
        else:
            print(answer)

    elif M>N:
        if M%diff==0:
            Maxidx=(M//diff)
        else:
            Maxidx=M
        idx=y
        
        for _ in range(Maxidx):
            
            if dp[idx]!=x:
                cnt+=1
            else:
                answer=y+N*cnt
                break

            idx-=diff

            if idx<=0:
                idx=M-abs(idx)
        if answer==0:
            print(-1)
        else:
            print(answer)
    else:
        if x==y:
            print(x)
        else:
            print(-1)
