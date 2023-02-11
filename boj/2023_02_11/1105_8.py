import sys

input=sys.stdin.readline().strip

L,R=input().split()
ans=0
if len(L)!=len(R):
    print(0)
else:
    for i in range(len(L)):
        if L[i]==R[i]:
            if L[i]=="8":
                ans+=1
        else:
            break
print(ans)


