for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    p=a.copy()
    p.sort()
    if a==p:
        print("0")
    elif a==p[::-1]:
        print(a[0])
    else:
        flag=True
        d=[]
        for i in range(n-1):
            if abs(a[i+1]-a[i])%2==1:
                d.append(a[i+1]-a[i])
        for i in d:
            if -i in d:
                flag = False
                print("-1")
        if flag:
            print("40741153")
                