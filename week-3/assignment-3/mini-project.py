day= input('What day is it? ').lower()
time= input('What time of day? ').lower()

if day == 'monday':
    if time == 'morning':
        print('Suggestion: Time to start your next Python lesson :) ')
    elif time == 'afternoon':
        print('Suggestion: Have a break with a snack.')
    elif time == 'evening':
        print('Time to wind down and review learning material.')
    else:
        print('Sorry, that\'s not a time.')

elif day == 'friday':
    if time == 'morning':
        print('Suggestion: Look back into the week and complete assignments.')
    elif time == 'afternoon':
        print('Suggestion: After completing assignments take a walk outside.')
    elif time == 'evening':
        print('Suggestion: Relax and watch a movie.')
    else:
        print('Sorry, that\'s not a time.')

elif day == 'sunday':
    if time == 'morning':
        print('Suggestion: Have breakfast outside today!')
    elif time == 'afternoon':
        print('Suggestion: Do some art or other hobby.')
    elif time == 'evening':
        print('Suggestion: Try cooking a new meal today.')
    else:
        print('Sorry, that\'s not a time.')

else: 
    print('Sorry, I don\'t recognize that day. Try Monday, Friday, or Sunday.')