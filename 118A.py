s=input().lower()
t=""
for i in s:
    if i not in 'aieouy':
        t=t+i
x=""
for i in t:
    x=x+"."+i
print(x)

