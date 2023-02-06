import sys
from collections import defaultdict
input=sys.stdin.readline

S,P=map(int,input().split())

s=input().strip()
A,C,G,T=map(int,input().split())
ans=0
if P < A+C+G+T:
    print(0)
    exit(0)
DNA=defaultdict(int)
for i in range(P):
    DNA[s[i]]+=1

if DNA["A"]>=A and DNA["C"]>=C and DNA["G"] >=G and DNA["T"] >=T:
    ans+=1
        
for i in range(1,S-P+1):
    DNA[s[i-1]]-=1
    DNA[s[i+P-1]]+=1
    
    if DNA["A"]>=A and DNA["C"]>=C and DNA["G"] >=G and DNA["T"] >=T:
        ans+=1

print(ans)
