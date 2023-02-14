n,m=map(int,input().split())
f=list (map(int,input().split()))
f.sort()
l=[]
i=0
j=n+1
for _ in range (m-n+1):
    l.append(f[i:j][n-1]-f[i:j][0])
    i+=1
    j+=1

print(min(l))