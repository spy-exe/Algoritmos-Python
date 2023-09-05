# 26) Receber do teclado, vários números e verificar se eles são ou não
# quadrados perfeitos. O programa termina quando o usuário digitar um 
# número menor ou igual a zero.

while True:
    num = int(input('Insira um número: '))
    if num <= 0:
        break
    else:
        raiz = num ** (1/2)
        if raiz == int(raiz):
            print(f'{num} é um quadrado perfeito!')
        else:
            print(f'{num} não é um quadrado perfeito!')