x=int(input())
z=0
k=30
while x>0:
    if x>=2**k:
        x-=2**k
        k-=1
        z+=1
    else:
        k-=1
print(z)