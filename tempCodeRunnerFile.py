     l=[(i,n-i) for i in range(1,n//2+1)]
        
        g=[]
        for i in l:
            g.append(lcm(i[0],i[1]))
        
        a=l[g.index(min(g))]
        for i in a:
            print(i,end=" ")