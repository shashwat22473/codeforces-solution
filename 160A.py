n=int(input())
a=list(map(int,input().split()))
a.sort()
a=a[::-1]
i=1
while True:
    if sum(a[:i])>sum(a)/2:
        print(i)
        break
    else:
        i+=1 

