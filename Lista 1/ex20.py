# 20) Apresentar o total da soma obtida dos cem primeiros números inteiros

numeros = []
count = 0
for i in range(1,100+1):
    count += 1
    numeros.append(count)
soma = sum(numeros)
print(soma)