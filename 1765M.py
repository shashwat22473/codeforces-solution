def lcm(a,b):
    if (a/b)%1==0:
        return(a)  
    elif (b/a)%1==0:
        return(b)
    else:
        c=a*b
        l=[i for i in range(1,min(a,b)+1)][::-1]
        for i in l:
            if  (c/i)%a==0 and (c/i)%b==0:
                return(c//i)

for _ in range(int(input())):
    n=int(input())
    if n%2==0:
        print(n//2 , n//2)
    else:
        l=[(i,n-i) for i in range(1,n//2+1)]
        
        g=[]
        for i in l:
            g.append(lcm(i[0],i[1]))
        
        a=l[g.index(min(g))]
        for i in a:
            print(i,end=" ")

    

        