n,t=map(int,input().split())
a = list(map(int,input().split()))
flag=True
i=1
while i <=n-1:
    if i==t:
        break
    else:
        i+=a[i-1]
if i==t:
    print("YES")
else:
    print("NO")

