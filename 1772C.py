for _ in range(int(input())):
    k,n=map(int,input().split())
    a=[]
    c=1
    i=1
    while c<=k:
        a.append(i)
        c+=1
        if n-((c**2-c+2))//2>=k-c:
            i=(c**2-c+2)//2
        else:
            i+=1
    for i in a:
        print(i,end=" ")
        
