print('This program finds the maximum integer out of three inputs')

a = int(input('Integer a : '))
b = int(input('Integer b : '))
c = int(input('Integer c : '))


def max3(a, b, c):
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c


print(f'maximum is {max3(a, b, c)}.')
