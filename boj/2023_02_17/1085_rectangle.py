import sys
input=sys.stdin.readline


x,y,w,h=map(int,input().split())

m=min(x-0,w-x,y-0,h-y)

print(m)

    