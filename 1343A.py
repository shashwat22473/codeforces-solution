for _ in range(int(input())):
    n=int(input())
    k=2
    if n%(2**k-1)==0:
        print(n//((2**k)-1))
    else:
        while n%(2**k-1)!=0:
            k+=1
        print(n//((2**k)-1))