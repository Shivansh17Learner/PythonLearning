num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
operation = input('Enter operation (+, -, *, /): ')
if operation == '+':
    result = num1 + num2    
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = 'Error: Division by zero'
else:
    result = 'Error: Invalid operation'
print('The result of', num1, operation, num2, 'is', result)