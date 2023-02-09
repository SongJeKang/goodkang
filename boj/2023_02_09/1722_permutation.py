import sys
import math
from collections import deque
input=sys.stdin.readline

N=int(input())
idx=[i for i in range(1,N+1)]
ipt=list(map(int,input().split()))

if ipt[0]==1:
    cmp=ipt[1]
    th=N
    ans=[]
    while cmp>=0 and th>0:
        num=0
        while(cmp>math.factorial(th-1)):
            cmp-=math.factorial(th-1)
            num+=1
        
        ans.append(num)

        th-=1
    result=[]
    for i in range(len(ans)):
        if ans[i]!=0:
            result.append(idx[ans[i]])
            idx.remove(idx[ans[i]])
        else:
            result.append(idx[0])
            idx.remove(idx[0])
    print(*result)
elif ipt[0]==2:
    ans=0
    for i in range(1,N+1):
        if ipt[i]==idx[0]:
            idx.remove(ipt[i])
            continue
        else:
            ans+=(idx.index(ipt[i]))*math.factorial(len(idx)-1)
            idx.remove(ipt[i])
            
        
    print(ans+1)


# if ans[i]!=0:
    #     if not queue:
    #         result.append(i+1+ans[i])
    #         idx.remove(i+1+ans[i])
    #     else:
    #         x=idx[0]
    #         result.append(x+ans[i])
    #         idx.remove(x+ans[i])
        
    #     if i+1 in idx:
    #         queue.append(i+1)
    # else:
    #     if not queue:
    #         result.append(i+1)
    #     else:
    #         x=queue.popleft()
    #         result.append(x)
    #         idx.remove(x)
    #         if i+1 in idx:
    #             queue.append(i+1)

