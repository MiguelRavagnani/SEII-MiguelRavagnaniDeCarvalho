# 
# Miguel Ravagnani de Carvalho
# 

#------------------------------------------------#
print("\n#------------------------------------------------#\n")
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)

#------------------------------------------------#
print("\n#------------------------------------------------#\n")

print(student['name'])

print(student.get('name'))

print(student.get('phone', 'Not found'))

#------------------------------------------------#
print("\n#------------------------------------------------#\n")

student['phone'] = '555-5555'
student['name'] = 'Jane'

print(student)
#------------------------------------------------#
print("\n#------------------------------------------------#\n")

student.update({'name': 'Jack', 'phone': '333-3333'})

print(student)
#------------------------------------------------#
print("\n#------------------------------------------------#\n")

age = student.pop('age')

print(age)
print(student)
#------------------------------------------------#
print("\n#------------------------------------------------#\n")

print(len(student))
print(student.keys())
print(student.items())

#------------------------------------------------#
print("\n#------------------------------------------------#\n")

for key, value in student.items():
    print(key, value)