for _ in range(int(input())):
    s="3141592653589793238462643383279"
    s_=input()
    t=0
    for i in range(len(s_)):
        if s[i]==s_[i]:
            t+=1
        else:
            break
    print(t)