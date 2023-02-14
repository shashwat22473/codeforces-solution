n,m=map(int,input().split())
l=[]
for _ in range(m):
    a=list(map(str,input().split()))
    l.append(a)
b=list(map(str,input().split()))
for i in b:
    for j in l:
        if i in j:
            if len(j[0])>len(j[1]):
                print(j[1],end=" ")
            else:
                print(j[0],end=" ")

