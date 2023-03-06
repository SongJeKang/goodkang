import sys
from collections import deque
input=sys.stdin.readline

while(1):
    q=[]
    s=input().rstrip()
    flag=True
    if s==".":
        break

    for i in range(len(s)):
        if s[i]=="(":
            q.append(s[i])

        elif s[i]==")":
            if not q:
                flag=False
                break
            elif q[-1]=="(":
                q.pop()
            else:
                q.clear()
                flag=False
                break
        
        elif s[i]=="[":
            q.append(s[i])
        
        elif s[i]=="]":
            if not q:
                flag=False
                break
            if q[-1]=="[":
                q.pop()
            else:
                q.clear()
                flag=False
                break
    
    if not flag:
        print("no")
        continue

    if q:
        print("no")
    else:
        print("yes")
