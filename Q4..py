M1=float(input('enter student 1 marks: '))
M2=float(input('enter student 2 marks: '))
M3=float(input('enter student 3 marks: '))
M4=float(input('enter student 4 marks: '))
M5=float(input('enter student 5 marks: '))
marks=[M1,M2,M3,M4,M5]#creating list
marks.sort()
marks.reverse()#sorting from high to low
print('marks in descending order',marks)
