def passs(s):
    x=0
    y=0
    for i in s:
        if i=="L":
            x-=1
        elif i=="R":
            x+=1
        elif i=="U":
            y+=1
        elif i=="D":
            y-=1
        if (x,y)==(1,1):
            return("YEs")
    return("NO")


for _ in range(int(input())):
    n=int(input())
    s=input()
    a=passs(s)
    print(a)
    