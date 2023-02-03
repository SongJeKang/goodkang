def find(x):
    global parent
    if parent[x] !=x:
        parent[x]=find(parent[x])
    
    return parent[x]
import sys
input=sys.stdin.readline

N=int(input())
parent=[i for i in range(N)]
v=[]
for i in range(N):
    s=list(map(int,input().split()))
    for j in range(i+1,N):
        v.append([i,j,s[j]])
v.sort(key=lambda x: x[2])

answer=0
for x in v:

    pi=find(x[0])
    pj=find(x[1])
    if pi==pj:
        continue

    parent[pj]=pi
    answer+=x[2]    
print(answer)

# while len(graph)<N-1 and v:
#     if not graph:
#         x=v.popleft()
#         graph.append(x)
#         parent[x[1]].add(parent[x[0]])
#         parent[x[0]].add(parent[x[1]])
#     else:
#         x=v.popleft()
    
#         if not(parent[x[0]].isdisjoint(parent[x[1]])):
#             continue
#         else:   
#             graph.append(x)
#             parent[x[1]].add(parent[x[0]])
#             parent[x[0]].add(parent[x[1]])
            


    






