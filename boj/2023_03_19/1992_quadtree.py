import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
def divide(y,x,size):
    global answer
    flag=mat[y][x]

    for i in range(y,y+size):
        for j in range(x,x+size):
            n=size//2
            if mat[i][j]!=flag:
                answer+="("
                divide(y,x,n)
                divide(y,x+n,n)
                divide(y+n,x,n)
                divide(y+n,x+n,n)
                answer+=")"
                return
        
    if flag=="0":
        answer+="0"
    else:
        answer+="1"

N=int(input())
mat=[]
for _ in range(N):
    mat.append(input().strip())
answer=''
divide(0,0,N)

print(answer)