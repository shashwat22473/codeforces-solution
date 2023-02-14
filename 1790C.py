def check(a):
    d={}
    for i in a :
        if len(i)!=0:
            if i[0] not in d:
                d[i[0]]=0
            d[i[0]]+=1
    a=list(d.keys())[list(d.values()).index(max(list(d.values())))]
    return(a) 
for _ in range(int(input())):
    a_=[]
    n=int(input())
    for i in range(n):
        a=list(map(int,input().split()))
        a_.append(a)
    a__=[]
    while len(a_[0])>0 or len(a_[1])>0:
        x=check(a_)
        a__.append(x)
        for j in a_:
            if x in j:
                j.remove(x)
        
    for i in a__:
        print(i,end=" ")