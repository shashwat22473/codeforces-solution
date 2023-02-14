n=int(input())
d={}
for i in range(n):
    a=tuple(map(int,input().split()))
    if a not in d:
        d[a]=1
    else:
        d[a]+=1
print(max(list(d.values())))