n,m=map(int,input().split())
a = list (map(int,input().split()))
sums=a[0]-1
for i in range(1,m):
    if a[i]-a[i-1]>=0:
        sums+=a[i]-a[i-1]
    else:
        sums+= n-a[i-1]+a[i]
print(sums)
