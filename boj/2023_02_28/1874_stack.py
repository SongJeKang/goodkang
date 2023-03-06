import sys
from collections import deque

input=sys.stdin.readline

N=int(input())
a=[i for i in range(N+1)]
num=deque(a)
stack=[]
arr=[]
answer=[]
num.popleft()

for _ in range(N):
    arr.append(int(input()))

for i in arr:
    if stack and i<stack[-1]:
        if stack[-1]!=i:
            print("NO")
            exit(0)
    elif stack and i==stack[-1]:
        stack.pop()
        answer.append("-")    
    else:
        while num:
            x=num.popleft()

            if x!=i:
                stack.append(x)
                answer.append("+")
            else:
                answer.append("+")
                answer.append("-")
                break

for i in answer:
    print(i)
