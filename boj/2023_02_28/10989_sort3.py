import sys

input=sys.stdin.readline

N=int(input())

arr=[0]*10001
for _ in range(N):
    arr[int(input())]+=1

for i in range(10001):
    if arr[i] !=0:
        for j in range(arr[i]):
            print(i)

# for i in range(N):
#     count[arr[i]]+=1

# for i in range(1,N+1):
#     count[i]+=count[i-1]

# result=[0 for _ in range(N)]

# for num in arr:
#     idx=count[num]
#     result[idx-1]=num
#     count[num]-=1

# print(result)
    
