import sys

input=sys.stdin.readline

N=int(input())
x_y=[]
for _ in range(N):
    a,b=map(int,input().split())

    x_y.append([a,b])


x_y.sort(key=lambda x: (x[1],x[0]))

for i in x_y:
    print(*i)