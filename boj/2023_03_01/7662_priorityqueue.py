import sys
import heapq
from collections import defaultdict
input=sys.stdin.readline

Test=int(input())

for _ in range(Test):
    k=int(input())
    q=[]
    q1=[]
    dic=defaultdict(int)
    cnt=0
    for i in range(k):
        s,num=input().split()
        if s[0]=='I':
            heapq.heappush(q,int(num))
            heapq.heappush(q1,-int(num))
            dic[int(num)]+=1
            cnt+=1
        if s[0]=='D':
            if q and q1:
                if num=='-1':
                    while q:
                        x=q[0]
                        if dic[x]==0:
                            heapq.heappop(q)
                        else:
                            heapq.heappop(q)
                            dic[x]-=1
                            break
                else:
                    while q1:
                        x=-q1[0]
                        if dic[x]==0:
                            heapq.heappop(q1)
                        else:
                            heapq.heappop(q1)
                            dic[x]-=1
                            break
                    
                cnt-=1
        if i==k-1:
            while q:
                    x=q[0]

                    if dic[x]<=0:
                        heapq.heappop(q)
                    else:
                        break
            while q1:
                x=-q1[0]

                if dic[x]<=0:
                    heapq.heappop(q1)                    
                else:
                    break
            if q and q1:
                print(-q1[0],q[0])
            else:
                print("EMPTY")