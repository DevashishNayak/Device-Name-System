dn=['switch','tv','switch','tv','switch','tv']
a=[]
b={}
for i in dn:
    if i not in a:
        a.append(i)
    else:
        if i+str(1) not in a:
            b[i]=1
            c=i+str(b[i])
            a.append(c)
        else:
            b[i]+=1
            c=i+str(b[i])
            a.append(c)
print(a)