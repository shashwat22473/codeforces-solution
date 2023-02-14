for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=1
    for i in a:
        b*=i
    if 2**n>=b:
        d=2**n%b
        if d!=0:
            print("-1")
        else:
            d_=2**n//b
            b_=reversed([i for i in range(2,len(a)+1)])
            count_=0
            for i in b_:
                if d_%i==0:
                    d_=d_//i
                    count_+=1
                if d_==0:
                    break
            print(count_)   
    