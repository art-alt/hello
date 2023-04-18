while True:
    x = int(input('Enter the first number: '))
    y = input('Enter the operation type: ')
    z = int(input('Enter the second number: '))
    if y == '+':
        print('Result: ', x + z)
    elif y == '-':
        print('Result: ', x - z)
    elif y == '*':
        print('Result: ', x * z)
    elif y == '/':
        while z == 0:
            print('Cannot divide by zero')
            break
        else:
            print('Result: ', x / z)




