import sys
from collections import defaultdict
input=sys.stdin.readline

Test=int(input())

for _ in range(Test):
    clothes=defaultdict(int)
    answer=1
    n=int(input())
    for i in range(n):
        s1,s2=map(str,input().split())
        if clothes[s2]:
            clothes[s2]+=1
        else:
            clothes[s2]=2
    for e in clothes.values():
        answer*=e

    print(answer-1)
