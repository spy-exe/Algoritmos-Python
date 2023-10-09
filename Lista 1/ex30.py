# 30) Ler um número do teclado e imprimir todos os números de 1 até o número 
# lido. Imprimir o produto dos números.

def produto(numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

num = int(input('Insira um valor: '))

count = 0
numeros = []
for i in range(1,num+1):
    count += 1
    numeros.append(count)
    print(count)

print(produto(numeros))