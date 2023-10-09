# 19) Apresentar os quadrados dos números inteiros de 15 a 200.

count = 15
for i in range(15,200+1):
    count += 1
    if (count % 5) == 0:
        print(count ** 2)
    else:
        continue
