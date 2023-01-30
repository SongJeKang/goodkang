import sys
from itertools import combinations
input=sys.stdin.readline

N,K=map(int,input().split())
dict={"a","c","i","n","t"}
cmp=set()
cmp.update(dict)
result=0
word=list()
for _ in range(N):
    s=input().strip()
    alpha=set()
    for i in range(4,len(s)-4):
        alpha.add(s[i])
        alpha-=dict
    if alpha:
        word.append(alpha)
    else:
        result+=1
if K <5 :
    print(0)
    exit(0)

for i in range(len(word)):
    cmp.update(word[i])
cmp=cmp-dict

answer=0
print(word)
if len(cmp)<K-5:
    n=len(cmp)
else:
    n=K-5
for pair in combinations(cmp,n):
    dict.update(set(pair))
    print(dict)
    cnt=0
    for i in range(len(word)):
        if word[i].issubset(dict):
            cnt+=1
    
    answer=max(answer,result+cnt)
    dict={"a","c","i","n","t"}

print(answer)
