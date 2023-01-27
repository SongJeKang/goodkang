import sys

input=sys.stdin.readline

s=input().strip()

a=0
m=1000
for i in range(len(s)):
    if s[i]=="a":
        a+=1
        
for i in range(len(s)):
    b=0
    for j in range(i,i+a):
        idx = j % len(s)
        if s[idx]=="b":
            b+=1


    m=min(m,b)
print(m)
