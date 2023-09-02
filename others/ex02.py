contador = 0

min = int(input('Digite o raio mínimo para uma sequência de números: '))
max = int(input('Digite o raio máximo para uma sequência de números: '))

for i in range(min,max+1):
    contador += 1
    print(contador)

print(contador)