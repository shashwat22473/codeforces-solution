for _ in range(int(input())):
    l,r,x=map(int,input().split())
    a,b=map(int,input().split())
    if b>=a:
        if r-l<x:
            if a==b:
                print("0")
            else:
                print("-1")
        else:
            if b-a>=x:
                print("1")
            
            elif a==b:
                print("0")
            elif b-a<x and a-l>=x:
                print("2")
            elif (b-a)<x and (a-l)<x and (r-a)>=x and (r-b)>=x:
                print("2")
            elif (b-a)<x and (a-l)<x and r-a>=x and b-l>=x:
                print("3")
            elif (b-a)<x and (a-l)<x and (r-a)>=x and b-l<x:
                print("-1")
            elif (b-a)<x and (a-l)<x and (r-a)<x:
                print("-1")
    if b<a:
        if r-l<x:
                print("-1")
        else:
            if a-b>=x:
                print("1")
            elif a-b<x and r-a>=x:
                print("2")
            elif (a-b)<x and (r-a)<x and (a-l)>=x and r-b>=x:
                print("3")
            elif (a-b)<x and (r-a)<x and (a-l)>=x and (r-a)>=x:
                print("2")
            elif (a-b)<x and (r-a)<x and (a-l)>=x and r-b<x:
                print("-1")
            elif (a-b)<x and (r-a)<x and (a-l)<x:
                print("-1")