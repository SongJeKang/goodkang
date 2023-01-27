import heapq
import sys

input=sys.stdin.readline

N=int(input())
l=[]

for _ in range(N):
    x=int(input())

    if x!=0:
        heapq.heappush(l,(abs(x),x))
    else:
        if not l:
            print(0)
        else:
            print(heapq.heappop(l)[1])