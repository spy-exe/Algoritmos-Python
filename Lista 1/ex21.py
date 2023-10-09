# 21) Apresentar todos os números divisíveis por 4 que sejam menores que 200.
count = 0
for i in range(1,200+1):
    count += 1
    if count % 4 == 0:
        print(count)
    else:
        continue
    