for _ in range(int(input())):
    t=0
    n=int(input())
    h=list(map(int,input().split()))
    h.sort(reverse=True)
    if 1 in h:
        a=h.index(1)
        t=a
        t+=(n-a)//2+(n-a)%2
        print(t)
    else:
        print(n)