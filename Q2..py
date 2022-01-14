#given constants
sd=10000 #standard deduction
depend_deduc=3000 #deduction per dependant
#user input
income=int(input('enter your gross income- '))#gross income
dependents=int(input('enter your no. of dependents- '))#no. of dependants
tax_income=int(income-sd-(3000*dependents))
tax=tax_income*(20/100)#tax rate=20%
print('your income tax is ',tax)
