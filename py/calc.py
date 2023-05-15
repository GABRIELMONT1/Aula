
num1_str = input('primeiro valor:')
num1 = int(num1_str)



num2_str = input('segundo valor:')
num2 = int(num2_str)


print(' Multiplicação [*]\n')
print(' Divisão [/]\n')
print(' Soma [+]\n')
print(' Subtração [-]\n')
ope = input('Tipo de operacao:')

if ope == '*':
    print('{} * {} ='.format(num1, num2))
    print(num1 * num2)

if ope == '/':
    print('{} / {} ='.format(num1, num2))
    print(num1 / num2)

if ope == '+':
    print('{} + {} ='.format(num1, num2))
    print(num1 + num2)

if ope == '-':
    print('{} - {} ='.format(num1, num2))
    print(num1 - num2)


    