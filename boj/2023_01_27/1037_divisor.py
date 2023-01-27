import sys

input=sys.stdin.readline

N=int(input())

l=list(map(int,input().split()))

l.sort()

if len(l)==1:
    print(l[0]*l[0])
else:
    print(l[0]*l[-1])