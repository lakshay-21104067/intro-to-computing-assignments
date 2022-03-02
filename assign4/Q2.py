print("With  iteration:")

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
#making ncr function
def ncr(n,r):
    x=factorial(n)/(factorial(n-r)*factorial(r))
    return int(x)    

row=int(input("Enter the nunber of rows:"))
i=1
while i<=row:
    print(" "*(row-i),end="")
    j=0
    while j<i:
        print(ncr(i-1,j)," ",end="")
        j+=1
    print("\n")
    i+=1

#pascal's triangle using recurssion

print("With recursion:")
def pascal_triangle(n,s,m):
    if n==0:
        print(" "*(s-1),1,"\n")
        return pascal_triangle(n+1,s,m)
    elif n==m:
        print("Done!")
        n=-1
    else:
        print(" "*(s-n),end="")
        x=0
        while x<=n:
            print(ncr(n,x),"",end="")
            x+=1
        print("\n")
        if n==m:
            n=-2
        return pascal_triangle(n+1,s,m)
    
        
m=int(input("Enter the no. of rows:"))
n=m-m
s=m+m
pascal_triangle(n,s,m)

