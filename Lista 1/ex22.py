# 22) Elaborar um programa que efetue a leitura sucessiva de valores numéricos 
# e apresente no final o total do somatório, a média e o total de valores lidos. 
# O programa deve fazer as leituras dos valores enquanto o usuário estiver 
# fornecendo valores positivos. Ou seja, o programa deve parar quando o 
# usuário fornecer um valor negativo.

numeros = []
count = 0
while True:
    count += 1
    num = int(input('Insira um numero:'))
    numeros.append(num)
    if num < 0:
        soma = sum(numeros)
        media = soma / count
        print(f'Programa encerrado.\n'
              f'Soma: {soma}\n'
              f'Media: {media}\n'
              f'Total de numeros: {count}\n')

