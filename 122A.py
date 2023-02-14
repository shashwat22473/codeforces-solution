n=int(input())
x=[4,7,44,47,74,77,444,447,477,474,744,747,774,777]
d=True
for i in x:
    if n%i==0:
        print("YES")
        d=False
        break
if d:
    print("NO")
