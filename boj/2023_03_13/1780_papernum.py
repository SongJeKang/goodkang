import sys
input=sys.stdin.readline
def checknum(y,x,size):
    global num1
    global num2
    global num3

    flag=mat[y][x]
    
    for i in range(y,y+size):
        for j in range(x,x+size):
            n=size//3
            
            if flag!=mat[i][j]:
                checknum(y,x,n)
                checknum(y,x+n,n)
                checknum(y,x+2*n,n)
                checknum(y+n,x,n)
                checknum(y+n,x+n,n)
                checknum(y+n,x+2*n,n)
                checknum(y+2*n,x,n)
                checknum(y+2*n,x+n,n)
                checknum(y+2*n,x+2*n,n)
                return
    if flag==-1:
        num1+=1
    elif flag==0:
        num2+=1
    else:
        num3+=1
N=int(input())
mat=[]
num1=0
num2=0
num3=0
for _ in range(N):
    mat.append(list(map(int,input().split())))

checknum(0,0,N)

print(num1)
print(num2)
print(num3)