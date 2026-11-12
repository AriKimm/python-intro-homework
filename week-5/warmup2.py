while True:
    user_input = input('Enter a postitive integer: ')

    try:
        number = int(user_input)

        if number > 0:
            print('Got it:', number)
            break
        else:
            print('That\'s not a postitve integer. Try again.')

    except ValueError:
        print('That\'s not a positive integer. Try again.')