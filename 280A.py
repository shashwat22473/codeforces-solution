s=input()
a=s.replace("WUB","_")
l=[]
u=""
for i in a:
    if i!="_":
        u=u+i
    if i=="_":
        if len(u)!=0:
            l.append(u)
            u=""
        
if u!="":
    l.append(u)
print(" ".join(l))