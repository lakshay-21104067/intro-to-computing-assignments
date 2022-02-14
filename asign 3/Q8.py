x = {1,2,3,4,5}#set1
y = {2,4,6,8}#set2
z = {1,5,9,13,17}#set3
print("set1=",x)
print("set2=",y)
print("set3=",z)
#(a)
a=x.symmetric_difference(y)
print("a.)",a)
#(b)
b = x^(y^z)
print("b.)",b)
#(c)
c = (x & y) | (y & z) | (y & x)
print("c.)",c)
#(d)
new_set={1,2,3,4,5,6,7,8,9,10}
d=new_set-x
print("d.)",d)
#(e)
e=new_set-(x|y|z)
print("e.)",e)
