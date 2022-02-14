term_one = int(input("1st number-"))
term_two = int(input("2nd number-"))
sum = term_one + term_two
series = [term_one,term_two]
n="y"
while(n=="y"):
    series.append(series[len(series)-1]+series[len(series)-2])
    print(series)
    n=input("Type y to continue and n to stop:")
print("The fibonacci series is")
print(series)

sum=0
for i in series:
    sum=sum+i
print("Average of the sequence")
print(sum/len(series))
