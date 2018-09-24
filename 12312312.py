import math as mat

print('Input first number: ', end = '')
a = int(input())

print('Input second number: ', end = '')
b = int(input())

print ('Input sign of operation: ', end = '')
c = input()

if c == '+':
    print(a, c, b, '=', a+b, sep = '\040', end = '')

elif c == '-':
    print(a, c, b, '=', a - b, sep='\040', end='')
elif c == '/':
    print(a, c, b, '=', a / b, sep='\040', end='')
elif c == '**':
    print(a, c, b, '=', a ** b, sep='\040', end='')
elif c == 'sqrt':
    print('sqrt(', a, ') = ', mat.sqrt(a))
    print('sqrt(', b, ') = ', mat.sqrt(b), end = '')
elif c == 'exp':
    print('exp(', a, ') = ', mat.exp(a))
    print('exp(', b, ') = ', mat.exp(b), end = '')
