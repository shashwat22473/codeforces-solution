for _ in range(int(input())):
    n,m,s_x,s_y,d=map(int,input().split())
    if abs(s_x-n) +abs(s_y-m)<=d:
        print("-1")
    elif (s_x-1)>d and (m-s_y)>d:
        print(n+m-2)
    elif (n-s_x)>d and (s_y-1)>d:
            print(n+m-2)
    else:
        print("-1")
    