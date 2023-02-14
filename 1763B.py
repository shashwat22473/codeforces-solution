for _ in range(int(input())):
    n,k=map(int,input().split())
    h=list(map(int,input().split()))
    p=list(map(int,input().split()))
    l=[[p[i],h[i]] for i in range(n)]
    l.sort(key = lambda x : x[0])
    n_=0
    while True:
        g=[]
        for i in range(len(l)):
            l[i][1]-=k
        for i in range(len(l)):
            if l[i][1]<=0:
                g.append(l[i])
        for i in g:
            if i in l:
                l.remove(i)
            
        
        if k<=0:
            n_+=1
            break
        elif len(l)==0:
            n_+=2
            break
        k-=l[0][0]
    if n_==1:
        print("NO")
    elif n_==2:
        print("YES")