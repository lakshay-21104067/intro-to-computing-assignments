student = dict()
answer = 'y'
while answer == 'y': 
    sid = int(input('SID: '))
    name = input('student name: ')
    student[sid] = name
    answer = input('y or n : ')

print(student)


b = int(input('SID: '))
print(student[b])

#sorting by SID
print(sorted(student.items()))
print(sorted((student)))

#sorting by name
newdict = dict()
for k,v in student.items():
    newdict[v] = k # reversing key value pairs
print(sorted(newdict.items()))
