import sys

input=sys.stdin.readline

N=int(input())
seq=[]
dp=[0 for _ in range(N)]
cnt=0
for _ in range(N):
    n=int(input())
    if n<0:
        cnt+=1
    seq.append(n)

seq.sort()
if seq[-1]<=0:
    seq.sort(reverse=True)
answer=0

while seq:
    x=seq.pop()
    if not seq:
        answer+=x
        break
    if x>1 and seq[-1] > 1:
        y=seq.pop()

        answer+=x*y
    elif x==0 and seq[-1] < 0:
        y=seq.pop()
        answer+=x*y
    elif x<0 and seq[-1]==0:
        y=seq.pop()
        answer+=x*y
    elif x<0 and seq[-1] <0:
        y=seq.pop()
        answer+=x*y
    else:
        answer+=x
    
    if seq and seq[-1]<=0:
        if cnt >1:
            seq.sort(reverse=True)
        
print(answer)
