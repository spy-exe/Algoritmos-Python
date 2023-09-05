# 23) Elaborar um programa que efetue a leitura de valores positivos inteiros até 
# que um valor negativo seja informado. Ao final devem ser apresentados o 
# maior e menor valore informados pelo usuário.

numeros = []
while True: 
    num = int(input('Insira um numero: '))
    numeros.append(num)
    if num < 0:
        print(f'Menor : {min(numeros)}\n'
              f'Maior : {max(numeros)}')
        
