student = {
    'name': 'Luna',
    'grade': 11,
    'subjects':['Biology','English', 'Spanish']
                 
}

for key, value in student.items():
    print(key,value)

student["graduated"] = False

print(student)