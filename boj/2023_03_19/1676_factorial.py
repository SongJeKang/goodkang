import sys

input=sys.stdin.readline

N=int(input())

ten=0
five=0
two=0

for i in range(1,N+1):
    cur=i
    while(cur>1):
        if cur%10==0:
            cur= cur//10
            ten+=1
        elif cur%5==0:
            five+=1
            cur= cur//5
        elif cur%2==0:
            two+=1
            cur=cur//2
        else:
            break

answer=min(two,five)+ten

print(answer)