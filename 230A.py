def bubbleSort(arr):
     
    n = len(arr)
 
    
    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return(arr)
s,n=map(int,input().split())
l=[]
for _  in range(n):
    a=list(map(int,input().split()))
    l.append(a)
a= bubbleSort(l)
flag=True
for  i in a:
    if s>i[0]:
        s+=i[1]
    else:
        print("NO")
        flag=False
        break
if flag:
    print("YES")

