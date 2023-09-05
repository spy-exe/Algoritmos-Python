# 27) Ler 2 valores e somar os dois. Caso a soma seja maior que 10, mostrar a soma.
numeros = []
for i in range(1,3):
    num = float(input(f'[{i}/2] Insira um valor: '))
    numeros.append(num)
    
soma = sum(numeros)
if soma > 10:
    print(f'A soma é maior que 10, portanto mostrando o resultado: {soma}')
else:
    print('Programa encerrado.')
        