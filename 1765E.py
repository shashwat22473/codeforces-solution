from math import ceil
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    if b>=a:
        print(ceil(n/a))
    else:
        print("1")