import sys
import re
from collections import deque
input=sys.stdin.readline

Test=int(input())

for _ in range(Test):
    p=input().strip()

    n=int(input())

    x=input().strip()

    x = x.replace('[', ',').replace(']', ',').split(',')[1:-1]
    q=deque(x)
    if q[0]=='':
        q.pop()
    flag=False
    an_flg=True
    for s in p:
        if s=='D':
            if not(q):
                an_flg=False
                break
            else:
                if flag:
                    q.pop()
                else:
                    q.popleft()
        elif s=='R':
            if flag:
                flag=False
            else:
                flag=True
        
    if an_flg:
        if flag==True:
            q.reverse()
            print("[" + ",".join(q) + "]")
        else:
            print("[" + ",".join(q) + "]")
    else:
        print("error")
