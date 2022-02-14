lst1 =[]
d = dict()
tpl =dict()
str = input('enter string : ')
seperate = str.split()
if len(seperate) == 1 :
    for i in str:
        lst1.append(i)
    for j in lst1:
        if j in d:
            d[j]=d[j]+1
        else:
            d[j]=1
    print(d)
else:
    for i in seperate:
        if i in tpl:
            tpl[i]+=1
        else:
            tpl[i]=1
    print(tpl)
