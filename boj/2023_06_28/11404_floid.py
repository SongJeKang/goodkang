import sys
input=sys.stdin.readline

n=int(input())

m=int(input())

city = [[1e9 for _ in range(n)] for _ in range(n)]

for _ in range(m):
   a,b,c = map(int,input().split())
   
   city[a-1][b-1]=min(city[a-1][b-1],c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            
            city[i][j] = min(city[i][j],city[i][k]+city[k][j])            

for i in range(n):
    for j in range(n):
        if city[i][j]==1e9:
            city[i][j]=0

for i in range(n):
    print(*city[i])

