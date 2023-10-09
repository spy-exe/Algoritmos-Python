# 05) Informar três números inteiros e imprimir a média.

numeros = []
for i in range(1,3+1):
    numero = int(input(f'[{i}/3] Insira um número: '))
    numeros.append(numero)
media = sum(numeros) / i
print(numeros, media)