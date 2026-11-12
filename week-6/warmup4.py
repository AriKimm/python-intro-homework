#Function for validating score
def is_valid_score(score):
    return isinstance(score, int) and 0 <= score <= 100

#Asks to enter a score
score= int(input('Enter your score: '))

#Checks if score is valid
if is_valid_score(score):
    print('Valid score.')
else:
    print('Invalid score ~ must be between 0 and 100 ~')
