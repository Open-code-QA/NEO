class CalcOptions():

    # Select option
    options = input("Select one option 'Add (+)', 'Subtract (-)', 'Multiply (*)', 'Divide (/)': ")
    # Enter first number
    first = int(input('Enter first number: '))
    # Enter second number
    second = int(input('Enter second number: '))

    # exceptions
    if options == 'Add' or '+':
        if type(first) != int or float:
            print('First number must be integer!')
    # add procedure
    if options == 'Add' or '+':
        print(first + second)
    # Subtract procedure
    elif options == 'Subtract' or '-':
        print(first - second)
    # Multiply procedure
    elif options == 'Multiply' or '*':
        print(first * second)
    # exceptions
    elif options == 'Divide' and second == 0:
        print('Division by zero!')
    # Divide procedure
    elif options == 'Divide' or '/':
        print(first / second)
    # exceptions
    else:
        print('Please, try again!')
