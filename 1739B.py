def check(d,n):
    l=[d[0]]
    for i in range(1,n):
        if d[i]<=l[-1] and d[i]!=0:
            return(False)
        else:
            if d[i]==0:
                l.append(l[-1])
            else:
                l.append(d[i]+l[-1])
    return(l) 
for _ in range(int(input())):
    n=int(input())
    d=list(map(int,input().split()))
    a=check(d,n)
    if a==False:
        print(-1)
    else:
        for i in a:
            print(i,end=" ")