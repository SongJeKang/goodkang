import sys

input=sys.stdin.readline
N=int(input())
ans=[]
idx=665
cnt=0
while True:
    idx+=1

    s=str(idx)

    for i in range(len(s)-2):
        if s[i]==s[i+1]==s[i+2]=="6":
            cnt+=1
            break

    if N==cnt:
        print(idx)
        break