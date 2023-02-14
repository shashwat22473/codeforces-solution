s=input()
if len(s)==1:
    if s.isupper()==True:
        print(s.lower())
    else:
        print(s.upper())
else:
    if s.isupper()==True:
        print(s.lower())
    elif s[0].islower()==True:
        flag=True
        for i in s[1:]:
            if i.islower()==True:
                flag=False
                print(s)
                break
        if flag:
            print(s[0].upper()+s[1:].lower())
    else:
        print(s)