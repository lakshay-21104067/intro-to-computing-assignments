x=float(input("Enter lenght of 1st side:"))
y=float(input("Enter lenght of 2nd side:"))
z=float(input("Enter lenght of 3rd side:"))
if x+y<=z:
    print("No, triangle cannot be formed")
elif x+z<=y:
    print("No, triangle cannot be formed")
elif y+z<=x:
    print("No, triangle cannot be formed")
else:
    print("Yes, triangle can be formed")
