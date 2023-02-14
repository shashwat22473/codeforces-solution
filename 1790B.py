for _ in range(int(input())):
    n,s,r=map(int,input().split())
    a=[]
    a.append(s-r)
    k=r//(n-1)
    z=r%(n-1)
    for i in range(z):
        a.append(k+1)
    for i in range(n-1-z):
        a.append(k)
    for i in a:
        print(i,end=" ")