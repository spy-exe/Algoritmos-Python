# 15) Ler um número e imprimir: maior que 20, igual a 20 ou menor que 20

num = float(input('Insira um numero: '))

if num > 20:
    print(f"{num} > 20")
elif num == 20:
    print(f"{num} = 20")
elif num < 20:
    print(f"{num} < 20")