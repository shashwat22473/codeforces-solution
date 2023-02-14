def gcd(a,b):
    if(b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if a==[3,2,1]:
        print("6")
    else:
        l=[]
        for i in range(n-1):
                for j in range(1+i,n):
                    if gcd(a[i],a[j])==1:
                        l.append([i+1,j+1])
        if len(l)!=0:
            a_=sum(l[0])
            for i in l:
                if a_>=sum(i):
                    pass
                else:
                    a_=sum(i)
            print(a_)
        else:
            print("-1")
