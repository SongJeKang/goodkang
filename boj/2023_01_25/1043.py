import sys
from collections import deque
N,M = map(int,input().split())

s = list(map(int,input().split()))
union = [set() for _ in range(N+1)]
trueman = set()
ans= 0
for i in range(1,s[0]+1):
    trueman.add(s[i])
party = list()

for x in range(M):
    party.append(list((map(int,input().split())))[1:])
    
for x in range(M):
    for y in range(len(party[x])):
        union[party[x][y]] |= set(party[x])

for i in range(1,len(union)):
    if union[i]:
        union[i].remove(i)

queue = deque()
queue.append(trueman)
while(queue):
    x = list(queue.popleft())
    for i in range(len(x)):
        if not(union[x[i]].issubset(trueman)):
            queue.append(union[x[i]])
            trueman |= union[x[i]]
        
# print(union)
# for i in range(1,N+1):
#     if not(trueman.isdisjoint(union[i])):
#         trueman |= union[i]
#         if len(union[i]) > 2:
#             for j in range(len(union[i])):
#                trueman |= union[union[i][j]]

for x in range(M):
    if set(party[x]).isdisjoint(trueman):
        ans+=1

print(ans)
# print(trueman)    
# for x in range(M):
#     flag=False
#     if len(party) > 2:
#         for i in trueman:
#             if flag==True:
#                 break
#             if i in party[x]:
#                 flag=True
#                 trueman |= set(party[x])
#                 break
        
#         if flag==False:
#             ans+=1
    
# print(ans)
# for i in range(len(party)):
#     if len(party[i]) > 2:

    
# flag=True
#     for i in range(len(party)):
#         if flag ==False:
#             break
#         for j in trueman:
#             if party[i] == j:
#                 flag=False
#                 break
#         if i==len(party)-1 and flag==True:
#             ans+=1
