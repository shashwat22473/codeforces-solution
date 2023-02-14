for _ in range(int(input())):
    n=int(input())
    sums=((n-1)*n*(2*n-1))//6 + (n*(n-1))//2 +(n*(n+1)*(2*n+1))//6
    print((sums*2022)%(10**9+7))      
       


