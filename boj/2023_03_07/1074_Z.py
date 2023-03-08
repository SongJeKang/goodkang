import sys

input=sys.stdin.readline
def z(row,col,n,cnt):
    global r,c,answer

    if n==1:
        print(row,col)
        answer=cnt+2*(r-row)+(c-col)
        return
    line=(2**(n-1))
    square=line**2

    if row<=r<row+line and col<=c<col+line:
        z(row,col,n-1,cnt)
    elif row<=r<row+line and col+line<=c<col+2*line:
        z(row,col+line,n-1,cnt+square)
    elif row+line<=r<row+2*line and col<=c<col+line:
        z(row+line,col,n-1,cnt+2*square)
    else:
        z(row+line,col+line,n-1,cnt+3*square)
N,r,c=map(int,input().split())

answer=0

z(0,0,N,0)
print(answer)
