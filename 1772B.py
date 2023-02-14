for _ in range(int(input())):
    flag=True
    l=[]
    for i in range(2):
        a=list (map(int,input().split()))
        l.append(a)
    for i in range(4):
        if l[1][1]>l[1][0]>l[0][0] and l[0][0]<l[0][1]<l[1][1]:
            print("YES")
            flag=False
            break
        else:
            l[0][0],l[0][1],l[1][0],l[1][1]=l[1][0],l[0][0],l[1][1],l[0][1]
    if flag:
        print("NO")