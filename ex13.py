# 13) Ler 1 número. Se positivo, imprimir raiz quadrada senão o quadrado. 

from math import sqrt
num = float(input('Insira um numero: '))
if num > 0:
    num = sqrt(num)
    print('O numero e positivo, portanto, sua raiz quadrada e: ')
else:
    num = num**2
    print('O numero e negativo, portanto, elevado quadrado e: ')
print(num)