n,m=map(int,input().split())
if m==n:
    print(n+1)
elif m>n:
    print(n)
else:
    print(n+((n//m)+n)//m)

