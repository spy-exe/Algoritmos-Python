# 28) Entrar com um número e imprimir a raiz quadrada do número. Caso ele 
# seja positivo. E o quadrado dele caso seja negativo.
from math import sqrt
num = float(input('Insira um valor: '))
if num > 0:
    raiz = sqrt(num)
    print(f'Exibindo raiz quadrada do número: {num}, = {raiz}')
elif num < 0:
    quadrado = num**2
    print(f'Exibindo o quadrado do número: {num}, = {quadrado}')