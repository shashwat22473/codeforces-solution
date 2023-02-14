n,a,b=map(int,input().split())
l=[f"x{i}" for i in range(n)]
g=set(l[a:])
h=set(l[n-b-1:])
print(len(g.intersection(h)))
    

