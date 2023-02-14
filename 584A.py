n,t=map(int,input().split())
s="1"
d_=""
flag=True
for i in range(n-1):
    s=s+"0"
for i in range(n):
    d_=d_+"9"
for i in range(int(s),int(d_)+1):
    if i%t==0:
        print(i)
        flag=False
        break
        
if flag:
    print("-1")   