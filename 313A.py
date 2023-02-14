n=int(input())
if n>0:
    print(n)
else:
    a=str(n)
    b=a[1:]
    c =b[:-1]
    d=b[:-2]+b[-1]
    if int(c)==0 or int(d)==0:
        print("0")
    elif int(c)>=int(d):
        print(f'-{int(d)}')
    else:
        print(f'-{int(c)}')