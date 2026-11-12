#Local scope
def dog_age():
    age= 14
    print(age)

dog_age()

#print(age)
#NameError: name 'age' is not defined

#'return' to access the value
def get_dog_age():
    age= 14
    return age

result= get_dog_age()
print(result)
