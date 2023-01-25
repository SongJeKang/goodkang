import sys
input=sys.stdin.readline

N,L=map(int,input().split())


while 1:
    s=0
    for i in range(L):
        s+=i

    if L > 100 or N-s < 0:
        print(-1)
        exit(0)

    elif (N-s) % L ==0:
        answer=[]
        start = (N-s) // L

        for j in range(L):
            answer.append(start+j)
        
        print(*answer)
        exit(0)
    else:
        L+=1

