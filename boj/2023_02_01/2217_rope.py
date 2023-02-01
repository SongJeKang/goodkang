import sys

input=sys.stdin.readline

N=int(input())
rope=[]

for _ in range(N):
    rope.append(int(input()))

rope.sort(reverse=True)

answer=0
for i in range(N):
    total=0
    answer=max(answer,rope[i]*(i+1))

print(answer)