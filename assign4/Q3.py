def fun(a,b):
    quotient=a//b
    remainder=a%b
    print("The quotient is:",quotient)
    print("The remainder is",remainder)
    result=[quotient,remainder]
    return result

a=int(input("Enter your first number:"))
b=int(input("Enter your second number-"))
result=fun(a,b)
print(result)
print("part(a)")
print("Callable:",callable(fun))

print("part(b)")
print("a is zero:",a==0)
print("b is zero:",b==0)
print("quotient is zero:",result[0]==0)
print("remainder is zero:",result[1]==0)
if(a==0):
    print("a is zero")

print("part(c)")
alist=[]
for i in result:
    if i>4:
        alist.append(i)
print("The values greater than 4 are:",alist)

print("part(d)")
aset=set(alist)
print(aset)

print("part(e)")
immutable_set=frozenset(aset)
print("The required immutable set",immutable_set)

print("part(f)")
maxval=0
for i in immutable_set:
    if i>maxval:
        maxval=i
print("The required max value is:",maxval)
print("The required hash value is:",hash(maxval))
