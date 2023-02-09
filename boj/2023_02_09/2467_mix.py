def bound(s,e):
    while(s<=e):

        mid=(s+e)//2

        if l[mid] <0:
            s=mid+1
        else:
            e=mid-1
        
    return s
import sys

input=sys.stdin.readline

N=int(input())

l=list(map(int,input().split()))

start=0
end=N-1
result=int(2e9)
cmp=int(2e9)
ans=[-1e9,1e9]
while start<end:
    result=l[start]+l[end]
    if result==0:
        print(l[start],l[end])
        exit(0)
    
    if cmp>abs(result):
        cmp=abs(result)

        ans[0],ans[1]=l[start],l[end]

    if result>0:
        end-=1
    else:
        start+=1

print(*ans)



#     if l[start] <0:
#         if history < l[start]+l[end]:
#             start+=1
#             end=N-1
#             history=int(2e9)
#         if l[end] >0:
#             if cmp>abs(l[start]+l[end]):
#                 cmp=abs(l[start]+l[end])
#                 ans[0]=l[start]
#                 ans[1]=l[end]
#                 if cmp==0:
#                     print(ans[0],ans[1])
#                     exit(0)
#             history=l[start]+l[end]
#             end-=1
#         else:
#             if cmp>abs(l[start]+l[end]):
#                 cmp=abs(l[start]+l[end])
#                 ans[0]=l[start]
#                 ans[1]=l[end]
#             history=(2e9)
#             start+=1
#             end=N-1
#     elif l[start] >=0:
#         if cmp>abs(l[start]+l[end]):
#                 cmp=abs(l[start]+l[end])
#                 ans[0]=l[start]
#                 ans[1]=l[start+1]
#                 break
