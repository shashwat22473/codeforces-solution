a,b=map(int,input().split())
n=a
m=a
while m>=b:
    n+=m//b
    m=m//b+m%b
print(n)