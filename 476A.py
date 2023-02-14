n,m=map(int,input().split())
if m>n:
    print("-1")
else:
    a=n//2+n%2
    flag=True
    while a<=n:
        if a%m==0:
            print(a)
            flag=False
            break
        else:
            a+=1
    if flag:
        print("-1")    