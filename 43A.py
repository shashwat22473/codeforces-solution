n=int(input())
lis=[]
for i in range(n):
    lis.append(input())
if len(set(lis))==1:
    print(lis[0])
else:
    a=lis.count(list(set(lis))[0])
    b=lis.count(list(set(lis))[1])
    if a>b:
        print(list(set(lis))[0])
    else:
        print(list(set(lis))[1])
    