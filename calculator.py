num1 = input('enter the first number: ')
num2 = input('enter the second number: ')
operation = input('enter the the operation(+ - * /): ')
num1 = int(num1)
num2 = int(num2)

if operation == '+':
    res = num1 + num2
    print('it is : ', res)
elif operation == '-':
    res = num1 - num2
    print('it is :', res)
elif operation == '*':
    res = num1 * num2
    print('it is: ')
elif operation == '/':
    res = num1 / num2
    print('it is :', res)


