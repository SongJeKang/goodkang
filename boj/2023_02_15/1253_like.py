import sys

input=sys.stdin.readline

N=int(input())

A=list(map(int,input().split()))
A.sort()
if len(A)<3:
    print(0)
    exit(0)
else:
    answer=0
    ans=set()        
    for i in range(N-1,-1,-1):
            if A[i] in ans:
                answer+=1
                continue

            start=0
            end=N-1

            while(start<end):

                if start==i:
                    start+=1
                    continue
                if end==i:
                    end-=1
                    continue

                if A[i]==A[start]+A[end]:
                    ans.add(A[i])
                    break
                elif A[i] < A[start]+A[end]:
                    end-=1
                else:
                    start+=1

        

answer+=len(ans)

print(answer)

