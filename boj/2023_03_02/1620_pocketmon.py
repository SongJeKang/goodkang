import sys
from collections import defaultdict
input=sys.stdin.readline

N,M=map(int,input().split())
dic1=defaultdict(int)
dic2=defaultdict(str)
for i in range(1,N+1):
    s=input().strip()

    dic1[s]=i
    dic2[i]=s
for _ in range(M):
    s1=input().strip()
    
    if ord(s1[0])<65:
        print(dic2[int(s1)])
    else:
        print(dic1[s1])
