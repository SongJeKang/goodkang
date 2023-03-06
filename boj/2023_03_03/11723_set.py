import sys
input=sys.stdin.readline

N=int(input())
a=set()
for _ in range(N):
    temp=input().strip().split()
    command=temp[0]
    if len(temp)>1:
        num=int(temp[1])
    if command=="add":
        a.add(int(num))

    elif command=="check":
        if {int(num)}.issubset(a):
            print(1)
        else:
            print(0)
    
    elif command=="remove":
        if {int(num)}.issubset(a):
            a.remove(int(num))
    
    elif command=="toggle":
        if {int(num)}.issubset(a):
            a.remove(int(num))
        else:
            a.add(int(num))
    elif command=="all":
        a=set({1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20})
    else:
        a.clear()
