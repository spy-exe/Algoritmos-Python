

entrada = int(input("Escolha um número entre 1 e 10: "))

while True:
    if entrada < 1 or entrada > 10:
        print(f"O número inserido: {entrada} não está entre 1 e 10, tente novamente.")
        break
    else:
        print(f"Você inseriu um número entre 1 e 10.\nNúmero escolhido: {entrada}")
        
