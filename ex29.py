# 29) Ler um número inteiro e verificar se está compreendido entre 20 e 80. Se 
# tiver, imprimir “parabéns”, senão imprimir “chimpanzé”.

valor = int(input('Insira um valor inteiro: '))
if valor >= 20 and valor <= 80:
    print('Parabéns!')
else:
    print('Chimpanzé!')