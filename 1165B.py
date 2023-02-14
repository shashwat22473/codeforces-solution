n=int(input())
a=list(map(int,input().split()))
a.sort()
k=0
while True:
    if len(a)==0:
        print(k)
        break
    a.append(k+1)
    a.sort()
    if a[-1]==k+1:
        if a[-2]!=k+1:
            print(k)
            break
        else:
            print(k+1)
            break
    else:
        if a.count(k+1)>1:
            a_=a[::-1].index(k+1)
            a=a[-(a_):]
            k+=1
        else:
            a_=a[::-1].index(k+1)
            a=a[-a_+1:]
            k+=1
        