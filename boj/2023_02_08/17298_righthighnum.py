import sys
input=sys.stdin.readline

N=int(input())

A=list(map(int,input().split()))
dp=[-1 for _ in range(N)]
stack=[A[-1]]
for i in range(N-2,-1,-1):

    while(stack):
        x=stack[-1]

        if A[i] < x:
            dp[i]=x
            stack.append(A[i])
            break
        else:
            stack.pop()

        if not stack:
            dp[i]=-1
            stack.append(A[i])
            break
        

dp[-1]=-1

print(*dp)
# for i in range(N-2,-1,-1):
#     if A[i+1] > A[i]:
#         stack.append(A[i+1])
#         dp[i]=A[i+1]        
#     elif dp[i+1]>A[i]:
#         dp[i]=dp[i+1]
#     elif
#     else:
#         for j in range(len(stack)-1,-1,-1):
#             if A[i] < stack[j]:
#                 dp[i]=stack[j]
#                 break
            
#             if j==0:
#                 dp[i]=-1
#     print(stack)
# dp[-1]=-1

# print(*dp)
