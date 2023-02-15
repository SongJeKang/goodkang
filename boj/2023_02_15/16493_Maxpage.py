def search(idx,day,page):
    global answer
    if N<day:
        return
    if idx==M:
        if day<=N:
            answer=max(answer,page)
            return

    search(idx+1,day,page)
    search(idx+1,day+chapter[idx][0],page+chapter[idx][1])

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
N,M=map(int,input().split())

chapter=[]
for _ in range(M):
    a,b=map(int,input().split())
    chapter.append([a,b])

answer=0
search(0,0,0)

print(answer)
