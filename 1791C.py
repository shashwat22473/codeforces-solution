for _ in range(int(input())):
    n=int(input())
    s=input()
    d_=[int(i) for i in s]
    while True:
        if len(d_)==0:
            print("0")
            break
        elif d_[0]==1 and d_[-1]==0: 
            d_=d_[1:-1]
        elif  (d_[0]==0 and d_[-1]==1):
            d_=d_[1:-1]
        else:
            print(len(d_))
            break