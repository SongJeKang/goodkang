import sys
input=sys.stdin.readline

N=int(input())

i=1
if N==1:
    print(1)
    exit(0)
else:
    N-=1
while 1:
    if (N-(6*i))<=0:
        break
    else:
        N-=6*i
    i+=1

print(i+1)