n = int(input())
sumx=0
sumy=0
sumz=0
for i in range(n):
    x,y,z=map(int,input().split())
    sumx+=x
    sumy+=y
    sumz+=z
if sumx==0 and sumy==0 and sumz==0:
    print("YES")
else:
    print("NO")
