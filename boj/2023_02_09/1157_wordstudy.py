import sys
from collections import defaultdict
input=sys.stdin.readline

s=input().strip()
alpha=defaultdict(int)
for i in range(len(s)):
    alpha[s[i].capitalize()]+=1

word=sorted(alpha.items(),key=lambda x: x[1], reverse=True)

if len(word) > 1 and word[0][1]==word[1][1]:
    print("?")
else:
    print(word[0][0])

