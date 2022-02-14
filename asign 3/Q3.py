def square(e):
    sqr = int(e)*int(e)
    return sqr
square(4)

lst = list(input('elements :\n'))
lst2 = []
for i in lst:
    lst2.append((i,square(i)))
print(lst2)
