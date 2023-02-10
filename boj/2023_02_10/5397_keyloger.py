import sys
from collections import deque
input=sys.stdin.readline

Test=int(input())

for _ in range(Test):
    q=deque()
    s=input().strip()
    cur=0

    ans=deque()
    for i in range(len(s)):
        if s[i] == "<":
            if ans:
                x=ans.pop()
                q.append(x)
        elif s[i] == ">":
            if q:
                x=q.pop()
                ans.append(x)
        elif s[i]=="-":
            if ans:
                ans.pop()
        else:
            ans.append(s[i])

        if i==len(s)-1:
            while q:
                x=q.pop()
                ans.append(x)

    print(*ans, sep="")
    

#         cmp1=''
#         cmp2=''
#         if s[i]=="<":
#             if cur >0:
#                 cur-=1

#         elif s[i]==">":
#             if cur <len(ans):
#                 cur+=1
#         elif s[i]=='-':
#             if 0<cur<len(ans):
#                 cmp1+=ans[cur:]
#                 cmp2+=ans[:cur-1]
#                 cur-=1
#                 ans=cmp1+cmp2
#             elif cur==len(ans):
#                 cmp1+=ans[:cur-1]
#                 ans=cmp1
#                 cur-=1
#         else:
#             if cur==len(ans):
#                 ans+=s[i]
#                 cur+=1
#             elif cur==0:
#                 ans=s[i]+ans
#                 cur+=1
#             else:
#                 cmp1+=ans[:cur]
#                 cmp2+=ans[cur:]
#                 cmp1+=s[i]
#                 ans=cmp1+cmp2
#                 cur+=1

# print(ans)

        