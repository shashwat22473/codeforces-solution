for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=""
    for i in a:
        b= b+str(i)
    if "-1-1" in b:
        print(sum(a)+4)
    elif "1-1" in b or"-11" in b :
        print(sum(a))
    elif "11" in b:
        print(sum(a)-4)
