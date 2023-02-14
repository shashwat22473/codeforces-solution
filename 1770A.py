from math import ceil
for _ in range(int(input())):
    n,m =map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    while True:
        a.sort()
        a.remove(a[0])
        a.append(b[0])
        b.remove(b[0])
        if len(b)==0:
            break
    print(sum(a))
    