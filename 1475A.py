for _ in range(int(input())):
    n=int(input())
    if n%2==1:
        print("yes")
    else:
        while n%2==0:
            n=n//2
        if n==1:
            print("no")
        else:
            print("yes")

