def init(node,start,end):

    if (start==end):
        tree[node]=arr[start]
        return tree[node]

    mid = start+end//2

    tree[node]=init(node*2,start,(start+end)//2)+init(node*2+1,(start+end)//2+1,end)
    return tree[node]
def update(node,start,end,index,diff):
    if index < start or index > end:
        return
    
    tree[node]+=diff

    if start !=end:
        mid = (start+end)//2

        update(node*2,start,mid,index,diff)
        update(node*2+1,mid+1,end,index,diff)
def subsum(node,start,end,left,right):
    if left>end or right < start:
        return 0

    if left<=start and end <=right:
        return tree[node]

    return subsum(node*2,start,(start+end)//2,left,right)+subsum(node*2+1,(start+end)//2+1,end,left,right)

import sys
import math
input=sys.stdin.readline
arr=[]
N,M,K = map(int,input().split())
for i in range(N):
    arr.append(int(input()))
h=int(math.ceil(math.log2((N))))

tree=[0 for _ in range(1<<(h+1))]

init(1,0,N-1)

for _ in range(M+K):
    a,b,c=map(int,input().split())

    if a==1:
        b=b-1
        diff=c-arr[b]
        arr[b]=c
        update(1,0,N-1,b,diff)
    else:
        print(subsum(1,0,N-1,b-1,c-1))