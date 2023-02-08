
import sys

input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
arr=A[:]

for i in range(N):
    for j in range(i):
        if A[i]>A[j] and arr[i]<arr[j]+A[i]:
            arr[i]=arr[j]+A[i]

print(max(arr))
