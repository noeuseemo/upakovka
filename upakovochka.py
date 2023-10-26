a = open('studentss.txt',encoding = 'utf-8')
students = []
for student in a:
    line = student.split(';')
    students.append({'id':int(line[0]), 'name':line[1], 'var':int(line[2]), 'subgroup':int(line[3])})

student1, _, _, student4, *_, lastStudent = students
*new_students, = student1, student4, lastStudent
print(new_students)

a.close()
