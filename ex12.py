# 12) Ler 2 números inteiros e soma-los. Se a soma for maior que 10, mostrar o 
# resultado da soma.


numeros = []
for i in range(1,2+1):
    numero = int(input(f'[{i}/2] Insira um numero: '))
    numeros.append(numero)
soma = sum(numeros)
if soma > 10:
    print(f"Soma dos numeros: {numeros} e igual a {soma}")
else:
    print("A soma nao foi maior que 10, portanto nenhum valor foi retornado.")
