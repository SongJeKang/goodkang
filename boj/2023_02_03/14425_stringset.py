import sys

input=sys.stdin.readline


N,M=map(int,input().split())

s_set=set()

for _ in range(N):
    s_set.add(input().strip())
answer=0
for _ in range(M):
    s=set([input().strip()])

    if s.issubset(s_set):
        answer+=1
    print(s_set,s)
print(answer)