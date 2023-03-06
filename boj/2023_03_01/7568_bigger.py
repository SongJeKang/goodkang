import sys
input=sys.stdin.readline

N=int(input())
lst=[]
answer=[0 for _ in range(N+1)]
for i in range(N):
    w,h=map(int,input().split())
    lst.append([w,h,0,i+1])

for i in range(N):
    for j in range(N):
        if i==j:
            continue
        
        if lst[i][0]<lst[j][0] and lst[i][1]<lst[j][1]:
            lst[i][2]+=1
        
for i in range(N):
    answer[lst[i][3]]=lst[i][2]+1
answer.remove(0)
print(*answer)
