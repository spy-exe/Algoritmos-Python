# 02) Receber um nome no teclado e imprimi-lo dez vezes.


nome = input('Insira um nome\n=> ')
count = 0
for i in range(1,10+1):
    count += 1
    print(count, nome)
