# 17) Criar um algoritmo que leia os limites inferior e superior de um intervalo e 
# imprimir todos os números pares no intervalo aberto e seu Somatório. Suponha que os dados digitados são para um intervalo
# crescente. 

min = int(input('Insira um valor minimo: '))
max = int(input('Insira um valor maximo: '))

count = 0
for i in range(min,max+1):
    count += 1
    if count % 2 == 0:
        print(count)
    else:
        continue

